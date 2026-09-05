<template>
  <router-link :to="`/applications/${app.id}`" class="card h-100 text-decoration-none text-dark shadow-sm">
    <div class="card-body">
      <div class="d-flex justify-content-between align-items-center">
        <strong>{{ app.applicant }}</strong>
        <ScoreBadge :score="app.score" />
      </div>
      <div class="mt-2 font-monospace">${{ app.amount.toLocaleString() }} · {{ app.status }}</div>
      <small class="text-muted">Updated {{ app.updatedAt }}</small>
    </div>
  </router-link>
</template>
<script setup>
import ScoreBadge from './ScoreBadge.vue'
defineProps({ app: { type: Object, required: true } })
</script>
