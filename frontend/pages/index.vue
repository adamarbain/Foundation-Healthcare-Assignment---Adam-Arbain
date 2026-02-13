<template>
  <div>
    <div class="mb-8">
      <h1 class="text-3xl font-bold text-gray-900">Consultation Records</h1>
      <p class="mt-2 text-sm text-gray-600">
        View and manage patient consultation notes
      </p>
    </div>

    <!-- Loading State -->
    <div v-if="pending" class="flex justify-center items-center py-12">
      <UIcon name="i-heroicons-arrow-path" class="w-8 h-8 animate-spin text-primary-600" />
    </div>

    <!-- Error State -->
    <UAlert
      v-else-if="error"
      color="red"
      variant="soft"
      title="Error loading consultations"
      :description="error.message"
      class="mb-6"
    />

    <!-- Empty State -->
    <div v-else-if="!consultations || consultations.length === 0" class="text-center py-12">
      <UIcon name="i-heroicons-clipboard-document-list" class="w-16 h-16 mx-auto text-gray-400 mb-4" />
      <h3 class="text-lg font-medium text-gray-900 mb-2">No consultations yet</h3>
      <p class="text-gray-600 mb-6">Get started by creating your first consultation note.</p>
      <UButton
        to="/consultations/new"
        icon="i-heroicons-plus"
        size="lg"
      >
        New Consultation
      </UButton>
    </div>

    <!-- Consultations Table -->
    <div v-else class="bg-white shadow-sm rounded-lg overflow-hidden">
      <div class="overflow-x-auto">
        <table class="min-w-full divide-y divide-gray-200">
          <thead class="bg-gray-50">
            <tr>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Patient Name
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Consultation Date
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Diagnosis Codes
              </th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Notes Preview
              </th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <tr
              v-for="consultation in consultations"
              :key="consultation.id"
              class="hover:bg-gray-50 cursor-pointer transition-colors"
              @click="viewConsultation(consultation)"
            >
              <td class="px-6 py-4 whitespace-nowrap">
                <div class="flex items-center">
                  <UIcon name="i-heroicons-user-circle" class="w-5 h-5 text-gray-400 mr-2" />
                  <span class="text-sm font-medium text-gray-900">
                    {{ consultation.patient_name }}
                  </span>
                </div>
              </td>
              <td class="px-6 py-4 whitespace-nowrap">
                <div class="text-sm text-gray-900">
                  {{ formatDate(consultation.consultation_date) }}
                </div>
                <div class="text-xs text-gray-500">
                  {{ formatTime(consultation.consultation_date) }}
                </div>
              </td>
              <td class="px-6 py-4">
                <div class="flex flex-wrap gap-2">
                  <UBadge
                    v-for="code in consultation.diagnosis_codes"
                    :key="code.id"
                    color="primary"
                    variant="soft"
                    size="xs"
                  >
                    {{ code.code }}
                  </UBadge>
                </div>
              </td>
              <td class="px-6 py-4">
                <div class="text-sm text-gray-600 max-w-md truncate">
                  {{ consultation.notes }}
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Total Count -->
      <div class="bg-gray-50 px-6 py-3 border-t border-gray-200">
        <p class="text-sm text-gray-700">
          Total: <span class="font-medium">{{ total }}</span> consultation{{ total !== 1 ? 's' : '' }}
        </p>
      </div>
    </div>

    <!-- Consultation Detail Modal -->
    <UModal v-model="isModalOpen">
      <UCard v-if="selectedConsultation">
        <template #header>
          <div class="flex items-center justify-between">
            <h3 class="text-lg font-semibold text-gray-900">
              Consultation Details
            </h3>
            <UButton
              color="gray"
              variant="ghost"
              icon="i-heroicons-x-mark"
              @click="isModalOpen = false"
            />
          </div>
        </template>

        <div class="space-y-4">
          <!-- Patient Name -->
          <div>
            <label class="text-xs font-medium text-gray-500 uppercase tracking-wider">Patient Name</label>
            <p class="mt-1 text-sm text-gray-900">{{ selectedConsultation.patient_name }}</p>
          </div>

          <!-- Consultation Date -->
          <div>
            <label class="text-xs font-medium text-gray-500 uppercase tracking-wider">Consultation Date</label>
            <p class="mt-1 text-sm text-gray-900">
              {{ formatDate(selectedConsultation.consultation_date) }} at {{ formatTime(selectedConsultation.consultation_date) }}
            </p>
          </div>

          <!-- Diagnosis Codes -->
          <div>
            <label class="text-xs font-medium text-gray-500 uppercase tracking-wider">Diagnosis Codes</label>
            <div class="mt-2 space-y-2">
              <div
                v-for="code in selectedConsultation.diagnosis_codes"
                :key="code.id"
                class="flex items-start space-x-2 text-sm"
              >
                <UBadge color="primary" variant="soft">
                  {{ code.code }}
                </UBadge>
                <span class="text-gray-700">{{ code.description }}</span>
              </div>
            </div>
          </div>

          <!-- Notes -->
          <div>
            <label class="text-xs font-medium text-gray-500 uppercase tracking-wider">Clinical Notes</label>
            <p class="mt-2 text-sm text-gray-900 whitespace-pre-wrap">{{ selectedConsultation.notes }}</p>
          </div>

          <!-- Created At -->
          <div class="pt-4 border-t border-gray-200">
            <p class="text-xs text-gray-500">
              Record created: {{ formatDate(selectedConsultation.created_at) }} at {{ formatTime(selectedConsultation.created_at) }}
            </p>
          </div>
        </div>
      </UCard>
    </UModal>
  </div>
</template>

<script setup lang="ts">
import type { Consultation, ConsultationListResponse } from '~/types'

definePageMeta({
  title: 'Consultations',
  middleware: ['auth']
})

const api = useApi()

// Fetch consultations
const { data, pending, error, refresh } = await useAsyncData<ConsultationListResponse>(
  'consultations',
  () => api.getConsultations()
)

const consultations = computed(() => data.value?.consultations || [])
const total = computed(() => data.value?.total || 0)

// Modal state
const isModalOpen = ref(false)
const selectedConsultation = ref<Consultation | null>(null)

// View consultation details
const viewConsultation = (consultation: Consultation) => {
  selectedConsultation.value = consultation
  isModalOpen.value = true
}

// Date formatting
const formatDate = (dateString: string) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric'
  })
}

const formatTime = (dateString: string) => {
  const date = new Date(dateString)
  return date.toLocaleTimeString('en-US', {
    hour: '2-digit',
    minute: '2-digit'
  })
}

// Auto-refresh on mount
onMounted(() => {
  // Refresh data when returning to this page
  refresh()
})
</script>
