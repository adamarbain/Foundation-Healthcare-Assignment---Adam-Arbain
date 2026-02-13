from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional
from .. import crud, schemas
from ..database import get_db

router = APIRouter(
    prefix="/diagnosis",
    tags=["diagnosis"]
)

@router.get("", response_model=schemas.DiagnosisSearchResponse)
def search_diagnosis_codes(
    search: Optional[str] = Query(None, description="Search term for diagnosis code or description"),
    limit: int = Query(50, ge=1, le=100, description="Maximum number of results"),
    db: Session = Depends(get_db)
):
    """
    Search for ICD-10 diagnosis codes by code or description.
    
    - **search**: Optional search term (searches both code and description)
    - **limit**: Maximum number of results to return (default: 50, max: 100)
    """
    try:
        results = crud.search_diagnosis_codes(db, search_term=search, limit=limit)
        return {
            "results": results,
            "total": len(results)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error searching diagnosis codes: {str(e)}")
