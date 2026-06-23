"""
Optional helper script to populate the database with sample patient
records for demos, screenshots, or manual testing.

Usage:
    python seed.py

This is safe to run multiple times -- it always adds new rows, it
never deletes existing data. To start completely fresh, delete
instance/health_records.db (or instance/<your custom name>.db) and
run the app once to recreate an empty database, then run this script.
"""

from app import create_app
from app.database import get_db
from app.ai_service import predict_health_risk

SAMPLE_PATIENTS = [
    # full_name, date_of_birth, email, glucose, haemoglobin, cholesterol
    ("Maria Gonzalez", "1990-05-14", "maria.gonzalez@example.com", 90.0, 14.0, 180.0),
    ("John Smith", "1975-01-22", "john.smith@example.com", 160.0, 10.0, 260.0),
    ("Aisha Khan", "1988-11-03", "aisha.khan@example.com", 110.0, 13.2, 205.0),
    ("Liam O'Brien", "1965-07-09", "liam.obrien@example.com", 98.0, 15.1, 190.0),
    ("Priya Patel", "2001-02-28", "priya.patel@example.com", 105.0, 12.8, 215.0),
]


def seed():
    app = create_app()
    with app.app_context():
        db = get_db()
        for full_name, dob, email, glucose, haemoglobin, cholesterol in SAMPLE_PATIENTS:
            remark, risk_level = predict_health_risk(glucose, haemoglobin, cholesterol)
            db.execute(
                """
                INSERT INTO patients
                    (full_name, date_of_birth, email, glucose, haemoglobin,
                     cholesterol, remarks, risk_level)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (full_name, dob, email, glucose, haemoglobin, cholesterol, remark, risk_level),
            )
        db.commit()
        print(f"Seeded {len(SAMPLE_PATIENTS)} sample patient records.")


if __name__ == "__main__":
    seed()
