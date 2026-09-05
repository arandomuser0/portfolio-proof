import axios from 'axios'

export const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:3001',
  timeout: 10000
})

api.interceptors.request.use((cfg) => {
  const token = localStorage.getItem('crm_token')
  if (token) cfg.headers.Authorization = `Bearer ${token}`
  return cfg
})

// Normalize errors to { message, status, fields } for stores/views
api.interceptors.response.use(
  (r) => r,
  (err) => {
    const status = err?.response?.status ?? 0
    if (status === 401) localStorage.removeItem('crm_token')
    const message =
      err?.response?.data?.message || (status === 0 ? 'Network error - is the API running?' : `Request failed (${status})`)
    return Promise.reject({ message, status, fields: err?.response?.data?.errors || {}, raw: err })
  }
)
