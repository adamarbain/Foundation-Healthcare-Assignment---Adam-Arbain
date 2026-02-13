from sqlalchemy.orm import Session
from sqlalchemy import or_
from . import models, schemas
from typing import List, Optional

# Diagnosis Code CRUD operations
def search_diagnosis_codes(db: Session, search_term: Optional[str] = None, limit: int = 50) -> List[models.DiagnosisCode]:
    """
    Search diagnosis codes by code or description
    """
    query = db.query(models.DiagnosisCode)
    
    if search_term:
        search_pattern = f"%{search_term}%"
        query = query.filter(
            or_(
                models.DiagnosisCode.code.ilike(search_pattern),
                models.DiagnosisCode.description.ilike(search_pattern)
            )
        )
    
    return query.limit(limit).all()

def get_diagnosis_code_by_id(db: Session, code_id: int) -> Optional[models.DiagnosisCode]:
    """
    Get a single diagnosis code by ID
    """
    return db.query(models.DiagnosisCode).filter(models.DiagnosisCode.id == code_id).first()

# Consultation CRUD operations
def create_consultation(db: Session, consultation: schemas.ConsultationCreate) -> models.Consultation:
    """
    Create a new consultation with associated diagnosis codes
    """
    # Get diagnosis codes
    diagnosis_codes = db.query(models.DiagnosisCode).filter(
        models.DiagnosisCode.id.in_(consultation.diagnosis_code_ids)
    ).all()
    
    # Create consultation
    db_consultation = models.Consultation(
        patient_name=consultation.patient_name,
        consultation_date=consultation.consultation_date,
        notes=consultation.notes,
        diagnosis_codes=diagnosis_codes
    )
    
    db.add(db_consultation)
    db.commit()
    db.refresh(db_consultation)
    
    return db_consultation

def get_consultations(db: Session, skip: int = 0, limit: int = 100) -> List[models.Consultation]:
    """
    Get all consultations, ordered by consultation date (newest first)
    """
    return db.query(models.Consultation)\
        .order_by(models.Consultation.consultation_date.desc())\
        .offset(skip)\
        .limit(limit)\
        .all()

def get_consultation_by_id(db: Session, consultation_id: int) -> Optional[models.Consultation]:
    """
    Get a single consultation by ID
    """
    return db.query(models.Consultation).filter(models.Consultation.id == consultation_id).first()

def get_consultations_count(db: Session) -> int:
    """
    Get total count of consultations
    """
    return db.query(models.Consultation).count()
