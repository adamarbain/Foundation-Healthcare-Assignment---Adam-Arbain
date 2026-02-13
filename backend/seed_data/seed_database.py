"""
Database seeding script for ICD-10 diagnosis codes and default doctor account
Run this script to populate the database with initial data
"""
import sys
from pathlib import Path

# Add parent directory to path to import app modules
sys.path.append(str(Path(__file__).parent.parent))

from app.database import SessionLocal, engine, Base
from app.models import DiagnosisCode, Doctor
from app.auth import get_password_hash
from icd10_codes import ICD10_CODES

def seed_diagnosis_codes():
    """Seed the database with ICD-10 diagnosis codes"""
    db = SessionLocal()
    
    try:
        # Check if data already exists
        existing_count = db.query(DiagnosisCode).count()
        
        if existing_count > 0:
            print(f"Database already contains {existing_count} diagnosis codes.")
            response = input("Do you want to clear and re-seed diagnosis codes? (yes/no): ")
            
            if response.lower() == 'yes':
                db.query(DiagnosisCode).delete()
                db.commit()
                print("Cleared existing diagnosis codes.")
            else:
                print("Skipping diagnosis codes seeding.")
                return
        
        # Insert diagnosis codes
        print(f"Seeding {len(ICD10_CODES)} ICD-10 diagnosis codes...")
        
        for code_data in ICD10_CODES:
            diagnosis_code = DiagnosisCode(
                code=code_data["code"],
                description=code_data["description"]
            )
            db.add(diagnosis_code)
        
        db.commit()
        print(f"✓ Successfully seeded {len(ICD10_CODES)} diagnosis codes!")
        
        # Verify
        total_count = db.query(DiagnosisCode).count()
        print(f"Total diagnosis codes in database: {total_count}")
        
    except Exception as e:
        print(f"Error seeding diagnosis codes: {e}")
        db.rollback()
    finally:
        db.close()

def seed_default_doctor():
    """Create a default doctor account for testing"""
    db = SessionLocal()
    
    try:
        # Check if any doctors exist
        existing_doctors = db.query(Doctor).count()
        
        if existing_doctors > 0:
            print(f"\nDatabase already contains {existing_doctors} doctor(s).")
            print("Skipping default doctor creation.")
            return
        
        # Create default doctor
        print("\nCreating default doctor account...")
        default_doctor = Doctor(
            username="doctor",
            email="doctor@cliniccare.com",
            full_name="Dr. John Smith",
            hashed_password=get_password_hash("password123"),
            is_active=True
        )
        
        db.add(default_doctor)
        db.commit()
        
        print("✓ Successfully created default doctor account!")
        print("\n" + "=" * 50)
        print("DEFAULT LOGIN CREDENTIALS:")
        print("  Username: doctor")
        print("  Password: password123")
        print("=" * 50)
        print("\n⚠️  IMPORTANT: Change this password in production!")
        
    except Exception as e:
        print(f"Error creating default doctor: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    print("ClinicCare Mini EMR - Database Seeding")
    print("=" * 50)
    
    # Create tables if they don't exist
    Base.metadata.create_all(bind=engine)
    
    # Seed diagnosis codes
    seed_diagnosis_codes()
    
    # Seed default doctor
    seed_default_doctor()
    
    print("\n✓ Database seeding complete!")
