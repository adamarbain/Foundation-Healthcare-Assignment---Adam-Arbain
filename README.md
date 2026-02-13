# ClinicCare Mini EMR

A minimal Electronic Medical Records (EMR) system for managing patient consultations with ICD-10 diagnosis codes. Built with FastAPI (backend) and Nuxt 3 (frontend).

## 📋 Features

- **JWT Authentication**: Secure doctor login with JWT tokens
- **User Management**: Doctor registration and profile management
- **ICD-10 Diagnosis Search**: Search from 100 pre-populated ICD-10 diagnosis codes
- **Consultation Management**: Create and view patient consultation notes
- **Real-time Search**: Debounced search functionality for diagnosis codes
- **Protected Routes**: Secure endpoints requiring authentication
- **Responsive UI**: Modern, clean interface built with Nuxt UI
- **RESTful API**: Well-documented FastAPI endpoints with automatic Swagger documentation
- **Input Validation**: Comprehensive validation using Pydantic models

## 🏗️ Project Structure

```
cliniccare-emr/
├── backend/                    # FastAPI Backend
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py            # FastAPI application
│   │   ├── database.py        # Database configuration
│   │   ├── models.py          # SQLAlchemy models
│   │   ├── schemas.py         # Pydantic schemas
│   │   ├── crud.py            # Database operations
│   │   ├── auth.py            # JWT authentication utilities
│   │   ├── dependencies.py    # Auth dependencies
│   │   └── routers/           # API route handlers
│   │       ├── auth_router.py # Authentication endpoints
│   │       ├── diagnosis.py
│   │       └── consultation.py
│   ├── seed_data/             # Database seed files
│   │   ├── icd10_codes.py     # 100 ICD-10 codes
│   │   └── seed_database.py   # Seeding script
│   ├── requirements.txt       # Python dependencies
│   └── .env.example          # Environment template
│
├── frontend/                  # Nuxt 3 Frontend
│   ├── pages/
│   │   ├── index.vue         # Consultations list
│   │   ├── login.vue         # Login/Register page
│   │   └── consultations/
│   │       └── new.vue       # New consultation form
│   ├── layouts/
│   │   └── default.vue       # Main layout with auth menu
│   ├── middleware/
│   │   └── auth.ts           # Authentication middleware
│   ├── composables/
│   │   ├── useAuth.ts        # Authentication composable
│   │   └── useApi.ts         # API client
│   ├── types/
│   │   └── index.ts          # TypeScript types
│   ├── nuxt.config.ts        # Nuxt configuration
│   ├── package.json          # Node dependencies
│   └── .env.example         # Environment template
│
└── README.md                 # This file
```

## 🛠️ Tech Stack

### Backend
- **Framework**: FastAPI 0.115.0
- **Database**: PostgreSQL / SQLite
- **ORM**: SQLAlchemy 2.0.36
- **Validation**: Pydantic 2.9.2
- **Authentication**: JWT (python-jose, passlib)
- **Migration**: Alembic 1.14.0

### Frontend
- **Framework**: Nuxt 3
- **UI Library**: Nuxt UI (Tailwind CSS based)
- **Language**: TypeScript
- **HTTP Client**: Native $fetch

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- Node.js 18 or higher
- PostgreSQL (optional, SQLite works too)

### Backend Setup

1. **Navigate to backend directory**:
   ```bash
   cd backend
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**:
   ```bash
   # Copy example env file
   cp .env.example .env
   
   # Edit .env and set your database URL
   # For SQLite (default):
   DATABASE_URL=sqlite:///./cliniccare.db
   
   # For PostgreSQL:
   # DATABASE_URL=postgresql://user:password@localhost:5432/cliniccare
   ```

5. **Seed the database**:
   ```bash
   python seed_data/seed_database.py
   ```

6. **Run the development server**:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

   The API will be available at:
   - API: http://localhost:8000
   - Swagger Docs: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

### Frontend Setup

1. **Navigate to frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Configure environment**:
   ```bash
   # Copy example env file
   cp .env.example .env
   
   # Edit .env if your backend runs on a different port
   NUXT_PUBLIC_API_BASE=http://localhost:8000/api
   ```

4. **Run the development server**:
   ```bash
   npm run dev
   ```

   The application will be available at: http://localhost:3000

5. **Login to the application**:
   - Navigate to http://localhost:3000
   - You'll be redirected to the login page
   - Use default credentials:
     - Username: `doctor`
     - Password: `password123`

## 🔐 Authentication

The application uses JWT (JSON Web Tokens) for secure authentication. All consultation endpoints require authentication.

**Default Login Credentials:**
- Username: `doctor`
- Password: `password123`

**⚠️ Important:** Change the default password or create a new account immediately!

For detailed authentication documentation, see [AUTHENTICATION.md](./AUTHENTICATION.md)

## 📚 API Documentation

### Base URL
```
http://localhost:8000/api
```

### Authentication Endpoints

#### Register (POST `/api/auth/register`)
Create a new doctor account.

#### Login (POST `/api/auth/login-json`)
Login with username and password to get JWT token.

#### Get Current User (GET `/api/auth/me`)
Get current authenticated doctor's information (requires auth).

### Consultation Endpoints (Protected)

**Note:** All endpoints below require authentication. Include JWT token in Authorization header:
```
Authorization: Bearer <your_token>
```

#### 1. Search Diagnosis Codes (No Auth Required)
```http
GET /api/diagnosis?search={term}
```

**Query Parameters**:
- `search` (optional): Search term for code or description
- `limit` (optional): Maximum results (default: 50, max: 100)

**Response**:
```json
{
  "results": [
    {
      "id": 1,
      "code": "E11.9",
      "description": "Type 2 diabetes mellitus without complications"
    }
  ],
  "total": 1
}
```

#### 2. Create Consultation (Requires Auth)
```http
POST /api/consultation
Authorization: Bearer <token>
```

**Request Body**:
```json
{
  "patient_name": "John Doe",
  "consultation_date": "2024-01-15T10:30:00",
  "notes": "Patient presents with...",
  "diagnosis_code_ids": [1, 5, 10]
}
```

**Response** (201 Created):
```json
{
  "id": 1,
  "patient_name": "John Doe",
  "consultation_date": "2024-01-15T10:30:00",
  "notes": "Patient presents with...",
  "created_at": "2024-01-15T10:35:00",
  "diagnosis_codes": [
    {
      "id": 1,
      "code": "E11.9",
      "description": "Type 2 diabetes mellitus without complications"
    }
  ]
}
```

#### 3. Get All Consultations (Requires Auth)
```http
GET /api/consultation
Authorization: Bearer <token>
```

**Query Parameters**:
- `skip` (optional): Number of records to skip (pagination)
- `limit` (optional): Maximum records to return (default: 100)

**Response**:
```json
{
  "consultations": [...],
  "total": 10
}
```

#### 4. Get Single Consultation (Requires Auth)
```http
GET /api/consultation/{id}
Authorization: Bearer <token>
```

**Response**:
```json
{
  "id": 1,
  "patient_name": "John Doe",
  "consultation_date": "2024-01-15T10:30:00",
  "notes": "Patient presents with...",
  "created_at": "2024-01-15T10:35:00",
  "diagnosis_codes": [...]
}
```

## 🗄️ Database Schema

### Tables

#### `diagnosis_codes`
| Column | Type | Constraints |
|--------|------|-------------|
| id | Integer | Primary Key |
| code | String(10) | Unique, Not Null |
| description | Text | Not Null |

#### `consultations`
| Column | Type | Constraints |
|--------|------|-------------|
| id | Integer | Primary Key |
| patient_name | String(255) | Not Null |
| consultation_date | DateTime | Not Null |
| notes | Text | Not Null |
| created_at | DateTime | Not Null, Default: now() |

#### `consultation_diagnoses` (Association Table)
| Column | Type | Constraints |
|--------|------|-------------|
| consultation_id | Integer | Foreign Key |
| diagnosis_code_id | Integer | Foreign Key |

**Relationship**: Many-to-Many between Consultations and Diagnosis Codes

## 🧪 Testing the Application

### Using Swagger UI

1. Start the backend server
2. Navigate to http://localhost:8000/docs
3. Try the endpoints interactively

### Manual Testing Flow

1. **Start both servers** (backend on :8000, frontend on :3000)
2. **Open frontend**: http://localhost:3000
3. **Create a consultation**:
   - Click "New Consultation" button
   - Fill in patient name
   - Search and select diagnosis codes
   - Add clinical notes
   - Submit the form
4. **View consultations**:
   - Return to home page
   - See the new consultation in the table
   - Click on a row to view details

## 🎨 UI Features

### Consultations List Page
- Responsive table layout
- Search functionality (planned)
- Click to view full details in modal
- Empty state for new users
- Loading states

### New Consultation Form
- Real-time diagnosis code search with debouncing
- Visual feedback for selected codes
- Date/time picker
- Multi-line notes textarea
- Form validation with error messages
- Success notifications

## 🔒 Security Features (Current)

- Input validation with Pydantic
- SQL injection prevention (SQLAlchemy ORM)
- CORS configuration
- Error handling with appropriate status codes

## 📝 Environment Variables

### Backend (.env)
```env
DATABASE_URL=sqlite:///./cliniccare.db
CORS_ORIGINS=http://localhost:3000,http://127.0.0.1:3000

# JWT Authentication
SECRET_KEY=your-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

**⚠️ Important:** Change `SECRET_KEY` to a secure random string in production!

### Frontend (.env)
```env
NUXT_PUBLIC_API_BASE=http://localhost:8000/api
```

## ✅ Implemented Features

- [x] JWT Authentication for doctors
- [x] User login/logout functionality
- [x] Doctor registration
- [x] Protected routes and endpoints

## 🚧 Future Enhancements

- [ ] Password reset functionality
- [ ] Two-factor authentication (2FA)
- [ ] Session management and token revocation
- [ ] Pagination for consultation list
- [ ] Advanced search and filters
- [ ] Export consultations to PDF
- [ ] Patient management system
- [ ] Appointment scheduling
- [ ] Medical history tracking

## 🐛 Troubleshooting

### Backend Issues

**Database connection error**:
- Check DATABASE_URL in .env
- Ensure PostgreSQL is running (if using PostgreSQL)
- Try using SQLite for simplicity

**Module import errors**:
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt` again

**CORS errors**:
- Verify CORS_ORIGINS includes your frontend URL
- Check that frontend is running on the expected port

### Frontend Issues

**API connection error**:
- Ensure backend is running
- Verify NUXT_PUBLIC_API_BASE in .env
- Check browser console for errors

**Module not found errors**:
- Delete `node_modules` and `.nuxt` folders
- Run `npm install` again
- Try `npm run dev` again

## 📄 License

This project is created for educational purposes as part of a technical assessment.

## 👤 Author

Foundation Healthcare Technical Assessment

---

**Note**: This is a minimal EMR system designed for demonstration purposes. For production use, additional security measures, authentication, authorization, and compliance with healthcare regulations (HIPAA, etc.) would be required.
