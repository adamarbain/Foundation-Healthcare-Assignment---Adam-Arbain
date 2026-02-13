# ClinicCare Mini EMR - Backend

FastAPI backend for the ClinicCare Mini EMR system.

## Quick Start

### 1. Setup Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
# Copy example environment file
cp .env.example .env

# Edit .env file with your settings
```

### 4. Seed Database

```bash
python seed_data/seed_database.py
```

This will populate the database with 100 ICD-10 diagnosis codes.

### 5. Run Development Server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:
- **API Base**: http://localhost:8000
- **Swagger Documentation**: http://localhost:8000/docs
- **ReDoc Documentation**: http://localhost:8000/redoc

## API Endpoints

### Health Check
- `GET /` - API information
- `GET /api/health` - Health check

### Diagnosis Codes
- `GET /api/diagnosis?search={term}` - Search diagnosis codes

### Consultations
- `POST /api/consultation` - Create new consultation
- `GET /api/consultation` - Get all consultations
- `GET /api/consultation/{id}` - Get specific consultation

## Database Configuration

### SQLite (Default)
```env
DATABASE_URL=sqlite:///./cliniccare.db
```

### PostgreSQL
```env
DATABASE_URL=postgresql://username:password@localhost:5432/cliniccare
```

## Project Structure

```
backend/
├── app/
│   ├── main.py           # FastAPI application
│   ├── database.py       # Database configuration
│   ├── models.py         # SQLAlchemy models
│   ├── schemas.py        # Pydantic schemas
│   ├── crud.py           # CRUD operations
│   └── routers/          # API routers
├── seed_data/            # Database seeding
└── requirements.txt      # Dependencies
```

## Dependencies

- **fastapi**: Web framework
- **uvicorn**: ASGI server
- **sqlalchemy**: ORM
- **pydantic**: Data validation
- **alembic**: Database migrations
- **psycopg2-binary**: PostgreSQL adapter
- **python-dotenv**: Environment variables

## Development

### Running Tests
```bash
# Add pytest to requirements.txt first
pytest
```

### Database Migrations
```bash
# Initialize Alembic (if needed)
alembic init alembic

# Create migration
alembic revision --autogenerate -m "description"

# Apply migration
alembic upgrade head
```

## Error Handling

The API returns standard HTTP status codes:
- `200`: Success
- `201`: Created
- `400`: Bad Request
- `404`: Not Found
- `422`: Validation Error
- `500`: Internal Server Error
