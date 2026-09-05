<template>
  <nav class="navbar navbar-expand bg-light border-bottom px-3">
    <router-link class="navbar-brand fw-bold" to="/">Ledgerly CRM</router-link>
    <div class="navbar-nav">
      <router-link class="nav-link" to="/">Dashboard</router-link>
      <router-link class="nav-link" to="/applications">Applications</router-link>
    </div>
  </nav>
  <main class="container py-4"><router-view /></main>
</template>
<script setup></script>
