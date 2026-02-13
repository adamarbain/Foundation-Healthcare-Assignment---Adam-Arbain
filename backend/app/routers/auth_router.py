"""
Authentication router for login, register, and user management
"""
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
from typing import List

from .. import models, schemas, auth
from ..database import get_db
from ..dependencies import get_current_active_doctor

router = APIRouter(
    prefix="/auth",
    tags=["authentication"]
)


@router.post("/register", response_model=schemas.DoctorResponse, status_code=status.HTTP_201_CREATED)
def register_doctor(
    doctor: schemas.DoctorCreate,
    db: Session = Depends(get_db)
):
    """
    Register a new doctor account
    """
    # Check if username already exists
    db_doctor = db.query(models.Doctor).filter(models.Doctor.username == doctor.username).first()
    if db_doctor:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )
    
    # Check if email already exists
    db_doctor = db.query(models.Doctor).filter(models.Doctor.email == doctor.email).first()
    if db_doctor:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Create new doctor
    hashed_password = auth.get_password_hash(doctor.password)
    new_doctor = models.Doctor(
        username=doctor.username,
        email=doctor.email,
        full_name=doctor.full_name,
        hashed_password=hashed_password,
        is_active=True
    )
    
    db.add(new_doctor)
    db.commit()
    db.refresh(new_doctor)
    
    # Create access token
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": new_doctor.username},
        expires_delta=access_token_expires
    )
    
    return {
        "doctor": new_doctor,
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.post("/login", response_model=schemas.Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """
    Login with username and password to get JWT token
    OAuth2 compatible endpoint (uses form data)
    """
    # Find doctor by username
    doctor = db.query(models.Doctor).filter(models.Doctor.username == form_data.username).first()
    
    if not doctor:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Verify password
    if not auth.verify_password(form_data.password, doctor.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Check if doctor is active
    if not doctor.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive account"
        )
    
    # Create access token
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": doctor.username},
        expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.post("/login-json", response_model=schemas.DoctorResponse)
def login_json(
    credentials: schemas.DoctorLogin,
    db: Session = Depends(get_db)
):
    """
    Login with JSON payload (alternative to form data)
    Returns doctor info along with token
    """
    # Find doctor by username
    doctor = db.query(models.Doctor).filter(models.Doctor.username == credentials.username).first()
    
    if not doctor:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    
    # Verify password
    if not auth.verify_password(credentials.password, doctor.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    
    # Check if doctor is active
    if not doctor.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive account"
        )
    
    # Create access token
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": doctor.username},
        expires_delta=access_token_expires
    )
    
    return {
        "doctor": doctor,
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get("/me", response_model=schemas.Doctor)
def get_current_user(
    current_doctor: models.Doctor = Depends(get_current_active_doctor)
):
    """
    Get current authenticated doctor's information
    """
    return current_doctor


@router.get("/doctors", response_model=List[schemas.Doctor])
def list_doctors(
    db: Session = Depends(get_db),
    current_doctor: models.Doctor = Depends(get_current_active_doctor)
):
    """
    List all doctors (requires authentication)
    """
    doctors = db.query(models.Doctor).all()
    return doctors
