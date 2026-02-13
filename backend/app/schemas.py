from pydantic import BaseModel, Field, field_validator, EmailStr
from datetime import datetime
from typing import List, Optional

# Doctor/Authentication Schemas
class DoctorBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    full_name: str = Field(..., min_length=1, max_length=255)

class DoctorCreate(DoctorBase):
    password: str = Field(..., min_length=6)

class DoctorLogin(BaseModel):
    username: str
    password: str

class Doctor(DoctorBase):
    id: int
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class DoctorResponse(BaseModel):
    doctor: Doctor
    access_token: str
    token_type: str

# Diagnosis Code Schemas
class DiagnosisCodeBase(BaseModel):
    code: str
    description: str

class DiagnosisCodeCreate(DiagnosisCodeBase):
    pass

class DiagnosisCode(DiagnosisCodeBase):
    id: int
    
    class Config:
        from_attributes = True

# Consultation Schemas
class ConsultationBase(BaseModel):
    patient_name: str = Field(..., min_length=1, max_length=255)
    consultation_date: datetime
    notes: str = Field(..., min_length=1)
    diagnosis_code_ids: List[int] = Field(..., min_items=1)
    
    @field_validator('patient_name')
    @classmethod
    def patient_name_not_empty(cls, v):
        if not v.strip():
            raise ValueError('Patient name cannot be empty')
        return v.strip()
    
    @field_validator('notes')
    @classmethod
    def notes_not_empty(cls, v):
        if not v.strip():
            raise ValueError('Notes cannot be empty')
        return v.strip()

class ConsultationCreate(ConsultationBase):
    pass

class Consultation(BaseModel):
    id: int
    patient_name: str
    consultation_date: datetime
    notes: str
    created_at: datetime
    diagnosis_codes: List[DiagnosisCode]
    
    class Config:
        from_attributes = True

# Response schemas
class DiagnosisSearchResponse(BaseModel):
    results: List[DiagnosisCode]
    total: int

class ConsultationListResponse(BaseModel):
    consultations: List[Consultation]
    total: int

class ErrorResponse(BaseModel):
    detail: str
