<template>
  <div class="language-selector">
    <label for="language">Select Language:</label>
    <select v-model="selectedLanguage" @change="changeLanguage">
      <option v-for="lang in languages" :key="lang.code" :value="lang.code">
        {{ lang.name }}
      </option>
    </select>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedLanguage: 'en',
      languages: [
        { code: 'en', name: 'English' },
        { code: 'hi', name: 'Hindi' },
        { code: 'ta', name: 'Tamil' },
        { code: 'te', name: 'Telugu' },
        { code: 'kn', name: 'Kannada' },
        { code: 'ml', name: 'Malayalam' },
        { code: 'bn', name: 'Bengali' },
        { code: 'mr', name: 'Marathi' },
        { code: 'gu', name: 'Gujarati' },
        { code: 'pa', name: 'Punjabi' },
        { code: 'or', name: 'Odia' },
      ],
    };
  },
  methods: {
    changeLanguage() {
      this.$emit('language-changed', this.selectedLanguage);
    },
  },
};
</script>

<style scoped>
.language-selector {
  margin: 1em 0;
}
</style>