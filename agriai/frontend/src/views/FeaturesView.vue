<template>
  <div class="features-view">
    <h1>Features</h1>
    <p>Explore the features of our application below:</p>
    <div class="feature-cards">
      <FeatureCard
        v-for="feature in features"
        :key="feature.id"
        :title="feature.title"
        :description="feature.description"
      />
    </div>
  </div>
</template>

<script>
import FeatureCard from '@/components/FeatureCard.vue';

export default {
  name: 'FeaturesView',
  components: {
    FeatureCard,
  },
  data() {
    return {
      features: [
        { id: 1, title: 'Feature One', description: 'Description of feature one.' },
        { id: 2, title: 'Feature Two', description: 'Description of feature two.' },
        { id: 3, title: 'Feature Three', description: 'Description of feature three.' },
      ],
    };
  },
};
</script>

<style scoped>
.features-view {
  padding: 20px;
}

.feature-cards {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}
</style>