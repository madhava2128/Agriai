<template>
  <div class="dashboard-view">
    <h1>Dashboard</h1>
    <DashboardPanel />
  </div>
</template>

<script>
import DashboardPanel from '@/components/DashboardPanel.vue';

export default {
  name: 'DashboardView',
  components: {
    DashboardPanel
  }
};
</script>

<style scoped>
.dashboard-view {
  padding: 20px;
}
</style>