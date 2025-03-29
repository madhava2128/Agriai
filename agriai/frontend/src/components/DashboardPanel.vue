<template>
  <div class="dashboard-panel">
    <h1>Dashboard</h1>
    <p>Welcome to the dashboard! Here you can find an overview of your activities.</p>
    <div class="stats">
      <div class="stat-item">
        <h2>Total Users</h2>
        <p>{{ totalUsers }}</p>
      </div>
      <div class="stat-item">
        <h2>Active Sessions</h2>
        <p>{{ activeSessions }}</p>
      </div>
      <div class="stat-item">
        <h2>Pending Tasks</h2>
        <p>{{ pendingTasks }}</p>
      </div>
    </div>
    <button @click="fetchData">Refresh Data</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      totalUsers: 0,
      activeSessions: 0,
      pendingTasks: 0,
    };
  },
  methods: {
    fetchData() {
      // Fetch data from the API and update the dashboard stats
      // Example API call (replace with actual API endpoint)
      fetch('/api/dashboard')
        .then(response => response.json())
        .then(data => {
          this.totalUsers = data.totalUsers;
          this.activeSessions = data.activeSessions;
          this.pendingTasks = data.pendingTasks;
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    },
  },
  mounted() {
    this.fetchData();
  },
};
</script>

<style scoped>
.dashboard-panel {
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.stats {
  display: flex;
  justify-content: space-around;
  margin-top: 20px;
}

.stat-item {
  text-align: center;
}

.stat-item h2 {
  margin: 0;
  font-size: 1.5em;
}

.stat-item p {
  font-size: 1.2em;
  color: #333;
}
</style>