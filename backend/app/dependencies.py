"""
FastAPI dependencies for authentication
"""
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from . import models, auth
from .database import get_db

# OAuth2 scheme for token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


def get_current_doctor(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> models.Doctor:
    """
    Get the current authenticated doctor from JWT token
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    # Decode token
    payload = auth.decode_access_token(token)
    if payload is None:
        raise credentials_exception
    
    username: str = payload.get("sub")
    if username is None:
        raise credentials_exception
    
    # Get doctor from database
    doctor = db.query(models.Doctor).filter(models.Doctor.username == username).first()
    if doctor is None:
        raise credentials_exception
    
    if not doctor.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user"
        )
    
    return doctor


def get_current_active_doctor(
    current_doctor: models.Doctor = Depends(get_current_doctor)
) -> models.Doctor:
    """
    Get the current active doctor (additional validation)
    """
    if not current_doctor.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive doctor account"
        )
    return current_doctor
