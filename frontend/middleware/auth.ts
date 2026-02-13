/**
 * Authentication middleware to protect routes
 */
export default defineNuxtRouteMiddleware((to, from) => {
  const { isAuthenticated } = useAuth()
  
  // If not authenticated and not going to login page, redirect to login
  if (!isAuthenticated.value && to.path !== '/login') {
    return navigateTo('/login')
  }
  
  // If authenticated and going to login page, redirect to home
  if (isAuthenticated.value && to.path === '/login') {
    return navigateTo('/')
  }
})
