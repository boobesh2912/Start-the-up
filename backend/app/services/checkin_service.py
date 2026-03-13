from datetime import datetime
from typing import List

from sqlalchemy.orm import Session

from ..models import Checkin, User


def create_checkin(db: Session, user_id: int, body: dict) -> Checkin:
    checkin = Checkin(
        user_id=user_id,
        update_text=body["update_text"],
        demo_link=body.get("demo_link"),
        progress=max(0, min(100, int(body["progress"]))),
        blocker=body.get("blocker"),
        created_at=datetime.utcnow(),
    )
    db.add(checkin)
    db.commit()
    db.refresh(checkin)
    return checkin


def get_user_checkins(db: Session, user_id: int) -> List[Checkin]:
    return (
        db.query(Checkin)
        .filter(Checkin.user_id == user_id)
        .order_by(Checkin.created_at.desc())
        .all()
    )


def get_builders(db: Session) -> List[dict]:
    users = db.query(User).filter(User.is_admin.is_(False)).all()
    result = []
    for user in users:
        latest = (
            db.query(Checkin)
            .filter(Checkin.user_id == user.id)
            .order_by(Checkin.created_at.desc())
            .first()
        )
        result.append(
            {
                "id": user.id,
                "name": user.name,
                "project_name": user.project_name,
                "cohort": user.cohort,
                "progress": latest.progress if latest else 0,
                "last_update": latest.created_at if latest else None,
                "demo_link": latest.demo_link if latest else None,
            }
        )
    result.sort(key=lambda x: x["progress"], reverse=True)
    return result


def get_launch_wall(db: Session) -> List[dict]:
    users = db.query(User).filter(User.is_admin.is_(False)).all()
    result = []
    for user in users:
        latest = (
            db.query(Checkin)
            .filter(Checkin.user_id == user.id)
            .order_by(Checkin.created_at.desc())
            .first()
        )
        if latest and latest.progress == 100:
            result.append(
                {
                    "id": user.id,
                    "name": user.name,
                    "project_name": user.project_name,
                    "demo_link": latest.demo_link,
                    "launched_at": latest.created_at,
                }
            )
    return result


def serialize_user(user: User) -> dict:
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "project_name": user.project_name,
        "cohort": user.cohort,
        "is_admin": user.is_admin,
        "created_at": user.created_at,
    }
