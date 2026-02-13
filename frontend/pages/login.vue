<template>
  <div class="min-h-screen bg-gradient-to-br from-primary-50 to-primary-100 flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full">
      <!-- Logo and Title -->
      <div class="text-center mb-8">
        <div class="flex justify-center mb-4">
          <div class="bg-primary-600 rounded-full p-3">
            <UIcon name="i-heroicons-clipboard-document-list" class="w-12 h-12 text-white" />
          </div>
        </div>
        <h2 class="text-3xl font-bold text-gray-900">
          ClinicCare EMR
        </h2>
        <p class="mt-2 text-sm text-gray-600">
          Sign in to access your account
        </p>
      </div>

      <!-- Login Card -->
      <div class="bg-white rounded-lg shadow-lg p-8">
        <!-- Tabs for Login/Register -->
        <div class="flex border-b border-gray-200 mb-6">
          <button
            @click="activeTab = 'login'"
            :class="[
              'flex-1 py-3 text-sm font-medium text-center border-b-2 transition-colors',
              activeTab === 'login'
                ? 'border-primary-600 text-primary-600'
                : 'border-transparent text-gray-500 hover:text-gray-700'
            ]"
          >
            Login
          </button>
          <button
            @click="activeTab = 'register'"
            :class="[
              'flex-1 py-3 text-sm font-medium text-center border-b-2 transition-colors',
              activeTab === 'register'
                ? 'border-primary-600 text-primary-600'
                : 'border-transparent text-gray-500 hover:text-gray-700'
            ]"
          >
            Register
          </button>
        </div>

        <!-- Login Form -->
        <form v-if="activeTab === 'login'" @submit.prevent="handleLogin" class="space-y-6">
          <!-- Error Alert -->
          <UAlert
            v-if="errorMessage"
            color="red"
            variant="soft"
            :title="errorMessage"
            :close-button="{ icon: 'i-heroicons-x-mark-20-solid' }"
            @close="errorMessage = ''"
          />

          <!-- Username -->
          <div>
            <label for="username" class="block text-sm font-medium text-gray-700 mb-2">
              Username
            </label>
            <UInput
              id="username"
              v-model="loginForm.username"
              placeholder="Enter your username"
              size="lg"
              icon="i-heroicons-user"
              :disabled="isLoading"
              required
            />
          </div>

          <!-- Password -->
          <div>
            <label for="password" class="block text-sm font-medium text-gray-700 mb-2">
              Password
            </label>
            <UInput
              id="password"
              v-model="loginForm.password"
              type="password"
              placeholder="Enter your password"
              size="lg"
              icon="i-heroicons-lock-closed"
              :disabled="isLoading"
              required
            />
          </div>

          <!-- Submit Button -->
          <UButton
            type="submit"
            size="lg"
            block
            :loading="isLoading"
            :disabled="isLoading"
          >
            Sign In
          </UButton>

          <!-- Default Credentials Info -->
          <div class="mt-4 p-3 bg-blue-50 border border-blue-200 rounded-lg">
            <p class="text-xs text-blue-800 font-medium mb-1">Default Credentials:</p>
            <p class="text-xs text-blue-700">Username: <code class="bg-blue-100 px-1 rounded">doctor</code></p>
            <p class="text-xs text-blue-700">Password: <code class="bg-blue-100 px-1 rounded">password123</code></p>
          </div>
        </form>

        <!-- Register Form -->
        <form v-else @submit.prevent="handleRegister" class="space-y-6">
          <!-- Error Alert -->
          <UAlert
            v-if="errorMessage"
            color="red"
            variant="soft"
            :title="errorMessage"
            :close-button="{ icon: 'i-heroicons-x-mark-20-solid' }"
            @close="errorMessage = ''"
          />

          <!-- Full Name -->
          <div>
            <label for="full_name" class="block text-sm font-medium text-gray-700 mb-2">
              Full Name
            </label>
            <UInput
              id="full_name"
              v-model="registerForm.full_name"
              placeholder="Dr. John Smith"
              size="lg"
              icon="i-heroicons-user-circle"
              :disabled="isLoading"
              required
            />
          </div>

          <!-- Username -->
          <div>
            <label for="reg_username" class="block text-sm font-medium text-gray-700 mb-2">
              Username
            </label>
            <UInput
              id="reg_username"
              v-model="registerForm.username"
              placeholder="Choose a username"
              size="lg"
              icon="i-heroicons-user"
              :disabled="isLoading"
              required
            />
          </div>

          <!-- Email -->
          <div>
            <label for="email" class="block text-sm font-medium text-gray-700 mb-2">
              Email
            </label>
            <UInput
              id="email"
              v-model="registerForm.email"
              type="email"
              placeholder="doctor@example.com"
              size="lg"
              icon="i-heroicons-envelope"
              :disabled="isLoading"
              required
            />
          </div>

          <!-- Password -->
          <div>
            <label for="reg_password" class="block text-sm font-medium text-gray-700 mb-2">
              Password (min 6 characters)
            </label>
            <UInput
              id="reg_password"
              v-model="registerForm.password"
              type="password"
              placeholder="Create a password"
              size="lg"
              icon="i-heroicons-lock-closed"
              :disabled="isLoading"
              required
            />
          </div>

          <!-- Submit Button -->
          <UButton
            type="submit"
            size="lg"
            block
            :loading="isLoading"
            :disabled="isLoading"
          >
            Create Account
          </UButton>
        </form>
      </div>

      <!-- Footer -->
      <p class="mt-6 text-center text-xs text-gray-500">
        ClinicCare Mini EMR &copy; {{ new Date().getFullYear() }}
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: false,
  title: 'Login'
})

const router = useRouter()
const { login, register, isAuthenticated } = useAuth()

// Redirect if already authenticated
if (process.client && isAuthenticated.value) {
  navigateTo('/')
}

const activeTab = ref<'login' | 'register'>('login')
const isLoading = ref(false)
const errorMessage = ref('')

// Login form
const loginForm = ref({
  username: '',
  password: ''
})

// Register form
const registerForm = ref({
  username: '',
  email: '',
  full_name: '',
  password: ''
})

// Handle login
const handleLogin = async () => {
  errorMessage.value = ''
  isLoading.value = true

  try {
    await login(loginForm.value.username, loginForm.value.password)
    
    // Redirect to home
    await navigateTo('/')
  } catch (error: any) {
    console.error('Login failed:', error)
    
    if (error.data?.detail) {
      errorMessage.value = error.data.detail
    } else if (error.message) {
      errorMessage.value = error.message
    } else {
      errorMessage.value = 'Login failed. Please check your credentials.'
    }
  } finally {
    isLoading.value = false
  }
}

// Handle register
const handleRegister = async () => {
  errorMessage.value = ''
  
  // Validate password length
  if (registerForm.value.password.length < 6) {
    errorMessage.value = 'Password must be at least 6 characters long'
    return
  }
  
  isLoading.value = true

  try {
    await register(registerForm.value)
    
    // Redirect to home
    await navigateTo('/')
  } catch (error: any) {
    console.error('Registration failed:', error)
    
    if (error.data?.detail) {
      errorMessage.value = error.data.detail
    } else if (error.message) {
      errorMessage.value = error.message
    } else {
      errorMessage.value = 'Registration failed. Please try again.'
    }
  } finally {
    isLoading.value = false
  }
}
</script>
