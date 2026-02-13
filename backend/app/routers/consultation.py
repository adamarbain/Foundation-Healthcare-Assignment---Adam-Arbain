from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas, models
from ..database import get_db
from ..dependencies import get_current_active_doctor

router = APIRouter(
    prefix="/consultation",
    tags=["consultation"]
)

@router.post("", response_model=schemas.Consultation, status_code=status.HTTP_201_CREATED)
def create_consultation(
    consultation: schemas.ConsultationCreate,
    db: Session = Depends(get_db),
    current_doctor: models.Doctor = Depends(get_current_active_doctor)
):
    """
    Create a new consultation note.
    
    - **patient_name**: Patient's full name (required)
    - **consultation_date**: Date and time of consultation (required)
    - **notes**: Consultation notes/observations (required)
    - **diagnosis_code_ids**: List of diagnosis code IDs (at least one required)
    """
    try:
        # Validate that all diagnosis codes exist
        for code_id in consultation.diagnosis_code_ids:
            diagnosis_code = crud.get_diagnosis_code_by_id(db, code_id)
            if not diagnosis_code:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Diagnosis code with ID {code_id} not found"
                )
        
        # Create the consultation
        db_consultation = crud.create_consultation(db, consultation)
        return db_consultation
    
    except HTTPException:
        raise
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating consultation: {str(e)}"
        )

@router.get("", response_model=schemas.ConsultationListResponse)
def get_consultations(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_doctor: models.Doctor = Depends(get_current_active_doctor)
):
    """
    Get all consultation notes, ordered by consultation date (newest first).
    
    - **skip**: Number of records to skip (for pagination)
    - **limit**: Maximum number of records to return
    """
    try:
        consultations = crud.get_consultations(db, skip=skip, limit=limit)
        total = crud.get_consultations_count(db)
        return {
            "consultations": consultations,
            "total": total
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving consultations: {str(e)}"
        )

@router.get("/{consultation_id}", response_model=schemas.Consultation)
def get_consultation(
    consultation_id: int,
    db: Session = Depends(get_db),
    current_doctor: models.Doctor = Depends(get_current_active_doctor)
):
    """
    Get a specific consultation by ID.
    """
    consultation = crud.get_consultation_by_id(db, consultation_id)
    if not consultation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Consultation with ID {consultation_id} not found"
        )
    return consultation
