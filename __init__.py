"""
Central configuration for the Flask app.

All values are read from environment variables (loaded from a local
.env file via python-dotenv) so that no secrets are hard-coded into
the source. See .env.example for the full list of supported variables.
"""

import os
from dotenv import load_dotenv

# Load variables from a .env file in the project root, if present.
# This must run before Config reads os.environ below.
load_dotenv()


class Config:
    """Base configuration shared by the whole application."""

    # Used by Flask to sign session cookies and CSRF tokens.
    # Falls back to a development-only default so the app still runs
    # out of the box, but a real deployment should always set this
    # via the .env file.
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only-change-this-key")

    # Path to the SQLite database file, relative to the project root.
    DATABASE_PATH = os.environ.get("DATABASE_PATH", "instance/health_records.db")

    # Optional API key for a real third-party health/AI API.
    # The app works fully offline without this (see app/ai_service.py).
    HEALTH_API_KEY = os.environ.get("HEALTH_API_KEY", "")

    # Reasonable defaults for form validation, kept here so they are
    # easy to tune in one place without hunting through view code.
    MIN_DATE_OF_BIRTH_YEAR = 1900
