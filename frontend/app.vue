<template>
  <div>
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </div>
</template>

<script setup lang="ts">
useHead({
  titleTemplate: (title) => title ? `${title} - ClinicCare` : 'ClinicCare Mini EMR'
})
</script>
