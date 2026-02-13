<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Navigation -->
    <nav class="bg-white shadow-sm border-b border-gray-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between h-16">
          <div class="flex items-center">
            <NuxtLink to="/" class="flex items-center space-x-3">
              <UIcon name="i-heroicons-clipboard-document-list" class="w-8 h-8 text-primary-600" />
              <span class="text-xl font-bold text-gray-900">ClinicCare</span>
            </NuxtLink>
          </div>
          
          <div class="flex items-center space-x-4">
            <NuxtLink
              to="/"
              class="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-gray-900 hover:bg-gray-100"
            >
              Consultations
            </NuxtLink>
            <NuxtLink
              to="/consultations/new"
              class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-primary-600 hover:bg-primary-700"
            >
              <UIcon name="i-heroicons-plus" class="w-4 h-4 mr-2" />
              New Consultation
            </NuxtLink>

            <!-- User Menu -->
            <UDropdown :items="userMenuItems" :popper="{ placement: 'bottom-end' }">
              <UButton color="gray" variant="ghost" class="flex items-center space-x-2">
                <UIcon name="i-heroicons-user-circle" class="w-5 h-5" />
                <span class="text-sm">{{ doctor?.full_name || 'Doctor' }}</span>
                <UIcon name="i-heroicons-chevron-down" class="w-4 h-4" />
              </UButton>
            </UDropdown>
          </div>
        </div>
      </div>
    </nav>

    <!-- Main Content -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <slot />
    </main>

    <!-- Footer -->
    <footer class="bg-white border-t border-gray-200 mt-auto">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        <p class="text-center text-sm text-gray-500">
          ClinicCare Mini EMR &copy; {{ new Date().getFullYear() }}
        </p>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
const { doctor, logout } = useAuth()
const router = useRouter()

const handleLogout = () => {
  logout()
  router.push('/login')
}

const userMenuItems = [
  [{
    label: doctor.value?.email || 'Email',
    icon: 'i-heroicons-envelope',
    disabled: true
  }],
  [{
    label: 'Logout',
    icon: 'i-heroicons-arrow-right-on-rectangle',
    click: handleLogout
  }]
]
</script>
