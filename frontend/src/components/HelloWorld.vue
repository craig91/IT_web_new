<script setup>
import { onMounted, ref } from 'vue'

const emails = ref([])

onMounted(async () => {
  try {
    const res = await fetch('http://localhost:8000/emails')
    const data = await res.json()
    console.log('Fetched Data:', data)
    console.log('Array type?', Array.isArray(data.emails))

    emails.value = data.emails
  } catch (error) {
    console.error('API call failed:', error)
  }
})
</script>

<template>
  <div>
    <h1>Email List</h1>
    <ul>
        <li v-for="email in emails" :key="email.id">
            {{ email.id }} - {{  email.email }}
        </li>
    </ul>
  </div>
</template>

<style>
h1 {
  color: darkblue;
}
</style>
