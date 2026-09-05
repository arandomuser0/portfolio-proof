<template>
  <h1 class="h4">Pipeline</h1>
  <div v-if="store.loading" class="placeholder-glow"><span class="placeholder col-6"></span></div>
  <div v-else-if="store.error" class="alert alert-danger">{{ store.error }}</div>
  <div v-else-if="!store.items.length" class="text-muted">No applications. Seed the mock API.</div>
  <div v-else class="row g-3">
    <div v-for="a in store.items" :key="a.id" class="col-md-4"><LoanCard :app="a" /></div>
  </div>
</template>
<script setup>
import { onMounted } from 'vue'
import { useApplicationsStore } from '../stores/applications'
import LoanCard from '../components/LoanCard.vue'
const store = useApplicationsStore()
onMounted(() => store.fetchAll())
</script>
