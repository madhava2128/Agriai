<template>
  <div class="feature-card">
    <h3 class="feature-title">{{ title }}</h3>
    <p class="feature-description">{{ description }}</p>
    <button @click="onFeatureClick" class="feature-button">Learn More</button>
  </div>
</template>

<script>
export default {
  name: 'FeatureCard',
  props: {
    title: {
      type: String,
      required: true
    },
    description: {
      type: String,
      required: true
    },
    onFeatureClick: {
      type: Function,
      required: true
    }
  }
}
</script>

<style scoped>
.feature-card {
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 16px;
  margin: 16px;
  text-align: center;
}

.feature-title {
  font-size: 1.5em;
  margin-bottom: 8px;
}

.feature-description {
  font-size: 1em;
  margin-bottom: 16px;
}

.feature-button {
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 10px 20px;
  cursor: pointer;
}

.feature-button:hover {
  background-color: #0056b3;
}
</style>