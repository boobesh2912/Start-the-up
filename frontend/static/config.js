(function () {
  const hostname = window.location.hostname;
  if (hostname === 'localhost' || hostname === '127.0.0.1') {
    window.API_BASE = 'http://localhost:8000';
  } else {
    window.API_BASE = 'https://YOUR_BACKEND.onrender.com';
  }
})();