import { defineStore } from 'pinia'
import { api } from '../api/client'

export const useApplicationsStore = defineStore('applications', {
  state: () => ({ items: [], detail: null, loading: false, error: null, filter: 'all' }),
  actions: {
    async fetchAll() {
      this.loading = true; this.error = null
      try {
        const q = this.filter === 'all' ? '' : `?status=${this.filter}`
        const { data } = await api.get(`/applications${q}`)
        this.items = data
      } catch (e) { this.error = e.message } finally { this.loading = false }
    },
    async fetchOne(id) {
      this.loading = true; this.error = null
      try { const { data } = await api.get(`/applications/${id}`); this.detail = data }
      catch (e) { this.error = e.message } finally { this.loading = false }
    },
    async decide(id, decision, note = '') {
      const { data } = await api.post(`/applications/${id}/decision`, { decision, note })
      this.detail = data
      await this.fetchAll()
      return data
    }
  }
})
