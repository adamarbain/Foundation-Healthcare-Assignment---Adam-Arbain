/**
 * Authentication composable for managing user login/logout and auth state
 */

import type { Doctor, DoctorResponse } from '~/types'

export const useAuth = () => {
  const config = useRuntimeConfig()
  const apiBase = config.public.apiBase
  
  // Auth state
  const token = useState<string | null>('auth-token', () => {
    if (process.client) {
      return localStorage.getItem('auth_token')
    }
    return null
  })
  
  const doctor = useState<Doctor | null>('auth-doctor', () => {
    if (process.client) {
      const doctorData = localStorage.getItem('doctor_data')
      return doctorData ? JSON.parse(doctorData) : null
    }
    return null
  })
  
  const isAuthenticated = computed(() => !!token.value)
  
  /**
   * Login with username and password
   */
  const login = async (username: string, password: string) => {
    try {
      const response: DoctorResponse = await $fetch(`${apiBase}/auth/login-json`, {
        method: 'POST',
        body: {
          username,
          password
        }
      })
      
      // Save token and doctor data
      token.value = response.access_token
      doctor.value = response.doctor
      
      if (process.client) {
        localStorage.setItem('auth_token', response.access_token)
        localStorage.setItem('doctor_data', JSON.stringify(response.doctor))
      }
      
      return response
    } catch (error: any) {
      console.error('Login error:', error)
      throw error
    }
  }
  
  /**
   * Register a new doctor account
   */
  const register = async (data: {
    username: string
    email: string
    full_name: string
    password: string
  }) => {
    try {
      const response: DoctorResponse = await $fetch(`${apiBase}/auth/register`, {
        method: 'POST',
        body: data
      })
      
      // Save token and doctor data
      token.value = response.access_token
      doctor.value = response.doctor
      
      if (process.client) {
        localStorage.setItem('auth_token', response.access_token)
        localStorage.setItem('doctor_data', JSON.stringify(response.doctor))
      }
      
      return response
    } catch (error: any) {
      console.error('Register error:', error)
      throw error
    }
  }
  
  /**
   * Logout and clear auth data
   */
  const logout = () => {
    token.value = null
    doctor.value = null
    
    if (process.client) {
      localStorage.removeItem('auth_token')
      localStorage.removeItem('doctor_data')
    }
  }
  
  /**
   * Get current doctor info from API
   */
  const getCurrentDoctor = async () => {
    if (!token.value) {
      throw new Error('Not authenticated')
    }
    
    try {
      const response: Doctor = await $fetch(`${apiBase}/auth/me`, {
        headers: {
          Authorization: `Bearer ${token.value}`
        }
      })
      
      doctor.value = response
      
      if (process.client) {
        localStorage.setItem('doctor_data', JSON.stringify(response))
      }
      
      return response
    } catch (error: any) {
      console.error('Get current doctor error:', error)
      // If unauthorized, clear auth data
      if (error.status === 401) {
        logout()
      }
      throw error
    }
  }
  
  /**
   * Check if user is authenticated and token is valid
   */
  const checkAuth = async () => {
    if (!token.value) {
      return false
    }
    
    try {
      await getCurrentDoctor()
      return true
    } catch (error) {
      return false
    }
  }
  
  return {
    token,
    doctor,
    isAuthenticated,
    login,
    register,
    logout,
    getCurrentDoctor,
    checkAuth
  }
}
