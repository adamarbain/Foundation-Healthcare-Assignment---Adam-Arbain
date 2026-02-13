from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

from .database import engine, Base
from .routers import diagnosis, consultation, auth_router

# Load environment variables
load_dotenv()

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="ClinicCare Mini EMR API",
    description="A minimal Electronic Medical Records system for managing patient consultations and ICD-10 diagnosis codes with JWT authentication",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
origins = os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router.router, prefix="/api")
app.include_router(diagnosis.router, prefix="/api")
app.include_router(consultation.router, prefix="/api")

@app.get("/")
def read_root():
    """
    Root endpoint - API health check
    """
    return {
        "message": "Welcome to ClinicCare Mini EMR API",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/api/health")
def health_check():
    """
    Health check endpoint
    """
    return {"status": "healthy"}
