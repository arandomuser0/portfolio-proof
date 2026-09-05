<template>
  <span class="badge" :class="cls">{{ label }}</span>
</template>
<script setup>
import { computed } from 'vue'
const props = defineProps({ score: { type: Number, required: true } })
const label = computed(() => props.score >= 720 ? `Prime · ${props.score}` : props.score >= 640 ? `Near-prime · ${props.score}` : `Subprime · ${props.score}`)
const cls = computed(() => props.score >= 720 ? 'text-bg-success' : props.score >= 640 ? 'text-bg-warning' : 'text-bg-danger')
</script>
