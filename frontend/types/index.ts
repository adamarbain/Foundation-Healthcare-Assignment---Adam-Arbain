/**
 * Type definitions for the application
 */

// Authentication types
export interface Doctor {
  id: number
  username: string
  email: string
  full_name: string
  is_active: boolean
  created_at: string
}

export interface DoctorResponse {
  doctor: Doctor
  access_token: string
  token_type: string
}

export interface Token {
  access_token: string
  token_type: string
}

// Diagnosis types
export interface DiagnosisCode {
  id: number
  code: string
  description: string
}

export interface DiagnosisSearchResponse {
  results: DiagnosisCode[]
  total: number
}

// Consultation types
export interface Consultation {
  id: number
  patient_name: string
  consultation_date: string
  notes: string
  created_at: string
  diagnosis_codes: DiagnosisCode[]
}

export interface ConsultationCreate {
  patient_name: string
  consultation_date: string
  notes: string
  diagnosis_code_ids: number[]
}

export interface ConsultationListResponse {
  consultations: Consultation[]
  total: number
}
