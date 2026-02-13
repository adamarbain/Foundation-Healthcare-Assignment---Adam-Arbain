<template>
  <div>
    <div class="mb-8">
      <NuxtLink
        to="/"
        class="inline-flex items-center text-sm text-gray-600 hover:text-gray-900 mb-4"
      >
        <UIcon name="i-heroicons-arrow-left" class="w-4 h-4 mr-1" />
        Back to Consultations
      </NuxtLink>
      <h1 class="text-3xl font-bold text-gray-900">New Consultation</h1>
      <p class="mt-2 text-sm text-gray-600">
        Record a new patient consultation with diagnosis codes
      </p>
    </div>

    <div class="bg-white shadow-sm rounded-lg p-6 max-w-3xl">
      <form @submit.prevent="handleSubmit" class="space-y-6">
        <!-- Patient Name -->
        <div>
          <label for="patient_name" class="block text-sm font-medium text-gray-700 mb-2">
            Patient Name <span class="text-red-500">*</span>
          </label>
          <UInput
            id="patient_name"
            v-model="formData.patient_name"
            placeholder="Enter patient's full name"
            size="lg"
            :disabled="isSubmitting"
            :class="{ 'border-red-500': errors.patient_name }"
          />
          <p v-if="errors.patient_name" class="mt-1 text-sm text-red-600">
            {{ errors.patient_name }}
          </p>
        </div>

        <!-- Consultation Date -->
        <div>
          <label for="consultation_date" class="block text-sm font-medium text-gray-700 mb-2">
            Consultation Date & Time <span class="text-red-500">*</span>
          </label>
          <UInput
            id="consultation_date"
            v-model="formData.consultation_date"
            type="datetime-local"
            size="lg"
            :disabled="isSubmitting"
            :class="{ 'border-red-500': errors.consultation_date }"
          />
          <p v-if="errors.consultation_date" class="mt-1 text-sm text-red-600">
            {{ errors.consultation_date }}
          </p>
        </div>

        <!-- Diagnosis Codes Search -->
        <div>
          <label for="diagnosis_search" class="block text-sm font-medium text-gray-700 mb-2">
            Diagnosis Codes (ICD-10) <span class="text-red-500">*</span>
          </label>
          
          <!-- Search Input -->
          <div class="relative">
            <UInput
              id="diagnosis_search"
              v-model="searchTerm"
              placeholder="Search by code or description..."
              size="lg"
              icon="i-heroicons-magnifying-glass"
              :disabled="isSubmitting"
              @input="handleSearch"
            />
            
            <!-- Search Results Dropdown -->
            <div
              v-if="showSearchResults && searchResults.length > 0"
              class="absolute z-10 mt-2 w-full bg-white border border-gray-200 rounded-lg shadow-lg max-h-64 overflow-y-auto"
            >
              <div
                v-for="code in searchResults"
                :key="code.id"
                class="px-4 py-3 hover:bg-gray-50 cursor-pointer border-b border-gray-100 last:border-b-0"
                @click="addDiagnosisCode(code)"
              >
                <div class="flex items-start justify-between">
                  <div class="flex-1">
                    <div class="flex items-center space-x-2 mb-1">
                      <UBadge color="primary" variant="soft" size="xs">
                        {{ code.code }}
                      </UBadge>
                      <span
                        v-if="isCodeSelected(code.id)"
                        class="text-xs text-green-600"
                      >
                        ✓ Selected
                      </span>
                    </div>
                    <p class="text-sm text-gray-700">{{ code.description }}</p>
                  </div>
                  <UButton
                    v-if="!isCodeSelected(code.id)"
                    size="xs"
                    color="gray"
                    variant="ghost"
                    icon="i-heroicons-plus"
                  />
                </div>
              </div>
            </div>

            <!-- No Results -->
            <div
              v-if="showSearchResults && searchResults.length === 0 && searchTerm"
              class="absolute z-10 mt-2 w-full bg-white border border-gray-200 rounded-lg shadow-lg p-4"
            >
              <p class="text-sm text-gray-600 text-center">No diagnosis codes found</p>
            </div>
          </div>

          <!-- Selected Codes -->
          <div v-if="selectedCodes.length > 0" class="mt-4">
            <p class="text-xs font-medium text-gray-500 uppercase tracking-wider mb-2">
              Selected Diagnosis Codes ({{ selectedCodes.length }})
            </p>
            <div class="space-y-2">
              <div
                v-for="code in selectedCodes"
                :key="code.id"
                class="flex items-start justify-between bg-primary-50 border border-primary-200 rounded-lg p-3"
              >
                <div class="flex-1">
                  <div class="flex items-center space-x-2 mb-1">
                    <UBadge color="primary">
                      {{ code.code }}
                    </UBadge>
                  </div>
                  <p class="text-sm text-gray-700">{{ code.description }}</p>
                </div>
                <UButton
                  color="red"
                  variant="ghost"
                  size="xs"
                  icon="i-heroicons-x-mark"
                  :disabled="isSubmitting"
                  @click="removeDiagnosisCode(code.id)"
                />
              </div>
            </div>
          </div>

          <p v-if="errors.diagnosis_codes" class="mt-2 text-sm text-red-600">
            {{ errors.diagnosis_codes }}
          </p>
        </div>

        <!-- Clinical Notes -->
        <div>
          <label for="notes" class="block text-sm font-medium text-gray-700 mb-2">
            Clinical Notes <span class="text-red-500">*</span>
          </label>
          <UTextarea
            id="notes"
            v-model="formData.notes"
            placeholder="Enter consultation notes, observations, treatment plan, etc."
            :rows="8"
            size="lg"
            :disabled="isSubmitting"
            :class="{ 'border-red-500': errors.notes }"
          />
          <p v-if="errors.notes" class="mt-1 text-sm text-red-600">
            {{ errors.notes }}
          </p>
        </div>

        <!-- Form Actions -->
        <div class="flex items-center justify-end space-x-4 pt-6 border-t border-gray-200">
          <UButton
            type="button"
            color="gray"
            variant="ghost"
            :disabled="isSubmitting"
            @click="navigateTo('/')"
          >
            Cancel
          </UButton>
          <UButton
            type="submit"
            size="lg"
            :loading="isSubmitting"
            :disabled="isSubmitting"
          >
            <UIcon name="i-heroicons-check" class="w-5 h-5 mr-2" />
            Save Consultation
          </UButton>
        </div>
      </form>

      <!-- Success Notification -->
      <div
        v-if="showSuccess"
        class="fixed bottom-4 right-4 z-50"
      >
        <UAlert
          color="green"
          variant="solid"
          title="Success!"
          description="Consultation saved successfully"
          :close-button="{ icon: 'i-heroicons-x-mark-20-solid' }"
          @close="showSuccess = false"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { DiagnosisCode, ConsultationCreate } from '~/types'

definePageMeta({
  title: 'New Consultation',
  middleware: ['auth']
})

const api = useApi()
const router = useRouter()

// Form state
const formData = ref({
  patient_name: '',
  consultation_date: '',
  notes: ''
})

// Diagnosis search state
const searchTerm = ref('')
const searchResults = ref<DiagnosisCode[]>([])
const selectedCodes = ref<DiagnosisCode[]>([])
const showSearchResults = ref(false)
const searchTimeout = ref<NodeJS.Timeout | null>(null)

// Form validation errors
const errors = ref<Record<string, string>>({})

// Submission state
const isSubmitting = ref(false)
const showSuccess = ref(false)

// Initialize with current date/time
onMounted(() => {
  const now = new Date()
  const year = now.getFullYear()
  const month = String(now.getMonth() + 1).padStart(2, '0')
  const day = String(now.getDate()).padStart(2, '0')
  const hours = String(now.getHours()).padStart(2, '0')
  const minutes = String(now.getMinutes()).padStart(2, '0')
  
  formData.value.consultation_date = `${year}-${month}-${day}T${hours}:${minutes}`
})

// Debounced search
const handleSearch = () => {
  showSearchResults.value = true
  
  if (searchTimeout.value) {
    clearTimeout(searchTimeout.value)
  }

  if (!searchTerm.value.trim()) {
    searchResults.value = []
    return
  }

  searchTimeout.value = setTimeout(async () => {
    try {
      const response = await api.searchDiagnosis(searchTerm.value)
      searchResults.value = response.results || []
    } catch (error) {
      console.error('Search error:', error)
      searchResults.value = []
    }
  }, 300) // 300ms debounce
}

// Check if code is already selected
const isCodeSelected = (codeId: number) => {
  return selectedCodes.value.some(code => code.id === codeId)
}

// Add diagnosis code
const addDiagnosisCode = (code: DiagnosisCode) => {
  if (!isCodeSelected(code.id)) {
    selectedCodes.value.push(code)
    errors.value.diagnosis_codes = ''
  }
  searchTerm.value = ''
  searchResults.value = []
  showSearchResults.value = false
}

// Remove diagnosis code
const removeDiagnosisCode = (codeId: number) => {
  selectedCodes.value = selectedCodes.value.filter(code => code.id !== codeId)
}

// Close search results when clicking outside
const handleClickOutside = (event: MouseEvent) => {
  const target = event.target as HTMLElement
  if (!target.closest('#diagnosis_search')) {
    showSearchResults.value = false
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
})

// Form validation
const validateForm = () => {
  errors.value = {}

  if (!formData.value.patient_name.trim()) {
    errors.value.patient_name = 'Patient name is required'
  }

  if (!formData.value.consultation_date) {
    errors.value.consultation_date = 'Consultation date is required'
  }

  if (selectedCodes.value.length === 0) {
    errors.value.diagnosis_codes = 'At least one diagnosis code is required'
  }

  if (!formData.value.notes.trim()) {
    errors.value.notes = 'Clinical notes are required'
  }

  return Object.keys(errors.value).length === 0
}

// Form submission
const handleSubmit = async () => {
  if (!validateForm()) {
    return
  }

  isSubmitting.value = true

  try {
    const payload: ConsultationCreate = {
      patient_name: formData.value.patient_name.trim(),
      consultation_date: new Date(formData.value.consultation_date).toISOString(),
      notes: formData.value.notes.trim(),
      diagnosis_code_ids: selectedCodes.value.map(code => code.id)
    }

    await api.createConsultation(payload)

    // Show success message
    showSuccess.value = true

    // Reset form
    formData.value = {
      patient_name: '',
      consultation_date: '',
      notes: ''
    }
    selectedCodes.value = []

    // Redirect after a short delay
    setTimeout(() => {
      router.push('/')
    }, 1500)

  } catch (error: any) {
    console.error('Submission error:', error)
    
    // Handle validation errors from backend
    if (error.data?.detail) {
      if (Array.isArray(error.data.detail)) {
        error.data.detail.forEach((err: any) => {
          const field = err.loc[err.loc.length - 1]
          errors.value[field] = err.msg
        })
      } else {
        alert(`Error: ${error.data.detail}`)
      }
    } else {
      alert('Failed to save consultation. Please try again.')
    }
  } finally {
    isSubmitting.value = false
  }
}
</script>
