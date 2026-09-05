<template>
  <div v-if="store.loading">Loading…</div>
  <div v-else-if="store.error" class="alert alert-danger">{{ store.error }}</div>
  <div v-else-if="store.detail">
    <h1 class="h4">{{ store.detail.applicant }}</h1>
    <ScoreBadge :score="store.detail.score" />
    <div class="mt-3 d-flex gap-2">
      <button class="btn btn-success" @click="decide('approved')">Approve</button>
      <button class="btn btn-outline-danger" @click="decide('rejected')">Reject</button>
    </div>
  </div>
</template>
<script setup>
import { onMounted } from 'vue'
import { useApplicationsStore } from '../stores/applications'
import ScoreBadge from '../components/ScoreBadge.vue'
const props = defineProps({ id: String })
const store = useApplicationsStore()
onMounted(() => store.fetchOne(props.id))
const decide = (d) => store.decide(props.id, d, 'Reviewed in demo')
</script>
