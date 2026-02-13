# ClinicCare Mini EMR - Frontend

Nuxt 3 frontend for the ClinicCare Mini EMR system.

## Quick Start

### 1. Install Dependencies

```bash
npm install
```

### 2. Configure Environment

```bash
# Copy example environment file
cp .env.example .env

# Edit .env if needed (default: http://localhost:8000/api)
```

### 3. Run Development Server

```bash
npm run dev
```

The application will be available at: http://localhost:3000

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run generate` - Generate static site
- `npm run preview` - Preview production build

## Project Structure

```
frontend/
├── pages/
│   ├── index.vue                 # Consultations list
│   └── consultations/
│       └── new.vue              # New consultation form
├── layouts/
│   └── default.vue              # Main layout with navigation
├── composables/
│   └── useApi.ts                # API client composable
├── types/
│   └── index.ts                 # TypeScript type definitions
├── nuxt.config.ts               # Nuxt configuration
└── package.json                 # Dependencies
```

## Features

### Consultations List Page (`/`)
- View all consultation records
- Responsive table layout
- Click rows to view full details
- Modal for detailed view
- Loading and error states
- Empty state for new users

### New Consultation Form (`/consultations/new`)
- Patient information input
- Real-time diagnosis code search
- Debounced search (300ms)
- Selected codes management
- Form validation
- Success notifications
- Automatic redirect after save

## UI Components

Uses Nuxt UI components built on Tailwind CSS:
- `UButton` - Buttons
- `UInput` - Text inputs
- `UTextarea` - Multi-line inputs
- `UBadge` - Diagnosis code badges
- `UModal` - Modal dialogs
- `UAlert` - Notifications
- `UIcon` - Icons from Heroicons

## API Integration

The `useApi` composable provides methods for:
- `searchDiagnosis(term)` - Search ICD-10 codes
- `getConsultations()` - Get all consultations
- `getConsultation(id)` - Get single consultation
- `createConsultation(data)` - Create new consultation

## TypeScript Types

Located in `types/index.ts`:
- `DiagnosisCode` - ICD-10 diagnosis code
- `Consultation` - Consultation record
- `ConsultationCreate` - New consultation payload
- Response types for API calls

## Styling

- **Framework**: Tailwind CSS (via Nuxt UI)
- **Icons**: Heroicons
- **Color Scheme**: Primary color with gray scale
- **Responsive**: Mobile-first design

## Environment Variables

```env
NUXT_PUBLIC_API_BASE=http://localhost:8000/api
```

## Development Tips

### Hot Module Replacement
Changes to Vue files will automatically reload in the browser.

### Type Checking
```bash
npm run build
```
This will check TypeScript types during the build process.

### Debugging
- Use Vue DevTools browser extension
- Check browser console for errors
- Network tab for API calls

## Troubleshooting

### Port Already in Use
```bash
# Use a different port
PORT=3001 npm run dev
```

### API Connection Issues
- Ensure backend is running on port 8000
- Check NUXT_PUBLIC_API_BASE in .env
- Verify CORS settings in backend

### Module Not Found
```bash
# Clear cache and reinstall
rm -rf node_modules .nuxt
npm install
npm run dev
```

## Build for Production

```bash
# Build application
npm run build

# Preview production build
npm run preview
```

## Deployment

The application can be deployed to:
- Vercel (recommended for Nuxt)
- Netlify
- AWS
- Any Node.js hosting platform

Configure environment variables in your deployment platform.
