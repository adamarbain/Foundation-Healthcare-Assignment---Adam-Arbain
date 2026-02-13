from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

# Association table for many-to-many relationship
consultation_diagnoses = Table(
    'consultation_diagnoses',
    Base.metadata,
    Column('consultation_id', Integer, ForeignKey('consultations.id', ondelete='CASCADE')),
    Column('diagnosis_code_id', Integer, ForeignKey('diagnosis_codes.id', ondelete='CASCADE'))
)

class Doctor(Base):
    __tablename__ = "doctors"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    full_name = Column(String(255), nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

class DiagnosisCode(Base):
    __tablename__ = "diagnosis_codes"
    
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(10), unique=True, index=True, nullable=False)
    description = Column(Text, nullable=False)
    
    # Relationship
    consultations = relationship(
        "Consultation",
        secondary=consultation_diagnoses,
        back_populates="diagnosis_codes"
    )

class Consultation(Base):
    __tablename__ = "consultations"
    
    id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String(255), nullable=False)
    consultation_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    notes = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    # Relationship
    diagnosis_codes = relationship(
        "DiagnosisCode",
        secondary=consultation_diagnoses,
        back_populates="consultations"
    )
