<template>
  <div class="home-view">
    <h1>Welcome to Agriai</h1>
    <p>Your one-stop solution for agricultural insights and translations.</p>
    <router-link to="/features" class="btn">Explore Features</router-link>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
};
</script>

<style scoped>
.home-view {
  text-align: center;
  margin-top: 50px;
}

.btn {
  display: inline-block;
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  text-decoration: none;
  border-radius: 5px;
}

.btn:hover {
  background-color: #45a049;
}
</style>