/**
 * Composable for API calls
 */

export const useApi = () => {
  const config = useRuntimeConfig()
  const apiBase = config.public.apiBase
  const { token } = useAuth()

  /**
   * Get auth headers with token
   */
  const getAuthHeaders = () => {
    const headers: Record<string, string> = {}
    if (token.value) {
      headers.Authorization = `Bearer ${token.value}`
    }
    return headers
  }

  /**
   * Search diagnosis codes
   */
  const searchDiagnosis = async (searchTerm: string = '') => {
    try {
      const url = searchTerm 
        ? `${apiBase}/diagnosis?search=${encodeURIComponent(searchTerm)}`
        : `${apiBase}/diagnosis`
      
      const response = await $fetch(url)
      return response
    } catch (error) {
      console.error('Error searching diagnosis codes:', error)
      throw error
    }
  }

  /**
   * Get all consultations
   */
  const getConsultations = async () => {
    try {
      const response = await $fetch(`${apiBase}/consultation`, {
        headers: getAuthHeaders()
      })
      return response
    } catch (error) {
      console.error('Error fetching consultations:', error)
      throw error
    }
  }

  /**
   * Get a single consultation by ID
   */
  const getConsultation = async (id: number) => {
    try {
      const response = await $fetch(`${apiBase}/consultation/${id}`, {
        headers: getAuthHeaders()
      })
      return response
    } catch (error) {
      console.error('Error fetching consultation:', error)
      throw error
    }
  }

  /**
   * Create a new consultation
   */
  const createConsultation = async (data: {
    patient_name: string
    consultation_date: string
    notes: string
    diagnosis_code_ids: number[]
  }) => {
    try {
      const response = await $fetch(`${apiBase}/consultation`, {
        method: 'POST',
        headers: getAuthHeaders(),
        body: data
      })
      return response
    } catch (error) {
      console.error('Error creating consultation:', error)
      throw error
    }
  }

  return {
    searchDiagnosis,
    getConsultations,
    getConsultation,
    createConsultation
  }
}
