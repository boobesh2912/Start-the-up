from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime, timedelta

from ..database import get_db
from ..models.checkin_form_model import CheckinForm, FormResponse
from ..models.user_model import User
from ..schemas.checkin_form_schema import (
    CheckinFormCreate, CheckinFormUpdate, CheckinFormResponse,
    FormResponseCreate, FormResponseOut, FormResponseWithUser
)
from ..services.auth_service import get_current_user, get_admin_user

router = APIRouter()


# ── ADMIN: Forms ──────────────────────────────────────────────────────────────

@router.post("/admin/forms", response_model=CheckinFormResponse)
def create_form(data: CheckinFormCreate, db: Session = Depends(get_db), admin: User = Depends(get_admin_user)):
    close_at = data.publish_at + timedelta(hours=24)
    form = CheckinForm(
        title=data.title,
        description=data.description,
        questions=[q.dict() for q in data.questions],
        publish_at=data.publish_at,
        close_at=close_at,
        created_by=admin.id
    )
    db.add(form)
    db.commit()
    db.refresh(form)
    return form


@router.get("/admin/forms", response_model=List[CheckinFormResponse])
def list_all_forms(db: Session = Depends(get_db), admin: User = Depends(get_admin_user)):
    return db.query(CheckinForm).order_by(CheckinForm.publish_at.desc()).all()


@router.put("/admin/forms/{form_id}", response_model=CheckinFormResponse)
def update_form(form_id: int, data: CheckinFormUpdate, db: Session = Depends(get_db), admin: User = Depends(get_admin_user)):
    form = db.query(CheckinForm).filter(CheckinForm.id == form_id).first()
    if not form:
        raise HTTPException(status_code=404, detail="Form not found")
    for field, value in data.dict(exclude_none=True).items():
        if field == "questions":
            value = [q if isinstance(q, dict) else q.dict() for q in value]
        setattr(form, field, value)
    form.close_at = form.publish_at + timedelta(hours=24)
    db.commit()
    db.refresh(form)
    return form


@router.delete("/admin/forms/{form_id}")
def delete_form(form_id: int, db: Session = Depends(get_db), admin: User = Depends(get_admin_user)):
    form = db.query(CheckinForm).filter(CheckinForm.id == form_id).first()
    if not form:
        raise HTTPException(status_code=404, detail="Form not found")
    db.delete(form)
    db.commit()
    return {"status": "deleted"}


@router.get("/admin/forms/{form_id}/responses", response_model=List[FormResponseWithUser])
def get_form_responses(form_id: int, db: Session = Depends(get_db), admin: User = Depends(get_admin_user)):
    form = db.query(CheckinForm).filter(CheckinForm.id == form_id).first()
    if not form:
        raise HTTPException(status_code=404, detail="Form not found")
    responses = db.query(FormResponse).filter(FormResponse.form_id == form_id).all()
    result = []
    for r in responses:
        user = db.query(User).filter(User.id == r.user_id).first()
        result.append(FormResponseWithUser(
            id=r.id, form_id=r.form_id, user_id=r.user_id,
            answers=r.answers, submitted_at=r.submitted_at,
            user_name=user.name if user else None,
            user_email=user.email if user else None,
            project_name=user.project_name if user else None
        ))
    return result


@router.delete("/admin/responses/{response_id}")
def delete_response(response_id: int, db: Session = Depends(get_db), admin: User = Depends(get_admin_user)):
    resp = db.query(FormResponse).filter(FormResponse.id == response_id).first()
    if not resp:
        raise HTTPException(status_code=404, detail="Response not found")
    db.delete(resp)
    db.commit()
    return {"status": "deleted"}


# ── USER: Active Form ─────────────────────────────────────────────────────────

@router.get("/forms/active", response_model=CheckinFormResponse)
def get_active_form(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    now = datetime.utcnow()
    form = db.query(CheckinForm).filter(
        CheckinForm.publish_at <= now,
        CheckinForm.close_at >= now
    ).order_by(CheckinForm.publish_at.desc()).first()
    if not form:
        raise HTTPException(status_code=404, detail="No active form right now")
    return form


@router.get("/forms/active/status")
def get_active_form_status(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    now = datetime.utcnow()
    form = db.query(CheckinForm).filter(
        CheckinForm.publish_at <= now,
        CheckinForm.close_at >= now
    ).order_by(CheckinForm.publish_at.desc()).first()
    if not form:
        return {"active": False, "form": None, "submitted": False}
    already = db.query(FormResponse).filter(
        FormResponse.form_id == form.id,
        FormResponse.user_id == current_user.id
    ).first()
    return {"active": True, "form_id": form.id, "form_title": form.title, "submitted": already is not None}


@router.post("/forms/{form_id}/respond", response_model=FormResponseOut)
def submit_response(form_id: int, data: FormResponseCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    now = datetime.utcnow()
    form = db.query(CheckinForm).filter(CheckinForm.id == form_id).first()
    if not form:
        raise HTTPException(status_code=404, detail="Form not found")
    if not (form.publish_at <= now <= form.close_at):
        raise HTTPException(status_code=400, detail="Form is not currently active")
    already = db.query(FormResponse).filter(
        FormResponse.form_id == form_id,
        FormResponse.user_id == current_user.id
    ).first()
    if already:
        raise HTTPException(status_code=409, detail="You already submitted this form")
    response = FormResponse(form_id=form_id, user_id=current_user.id, answers=data.answers)
    db.add(response)
    db.commit()
    db.refresh(response)
    return response


@router.get("/forms/my-responses", response_model=List[FormResponseOut])
def my_responses(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(FormResponse).filter(
        FormResponse.user_id == current_user.id
    ).order_by(FormResponse.submitted_at.desc()).all()