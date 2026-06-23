"""
Entry point for running the Health Prediction App locally.

Usage:
    python run.py

This starts Flask's built-in development server. Do not use this
server in production -- see README.md for production deployment notes
(e.g. gunicorn).
"""

from app import create_app

app = create_app()

if __name__ == "__main__":
    # debug=True enables auto-reload and detailed error pages during
    # development. Turn this off (or set FLASK_DEBUG=0) in production.
    app.run(debug=True, host="127.0.0.1", port=5000)
