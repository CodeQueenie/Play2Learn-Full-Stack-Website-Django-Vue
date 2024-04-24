<template>
  <router-view></router-view>
</template>

<script>
export default {
  name: 'App',
}
</script>

<!-- Uncomment this section if you want to use HelloWorld component -->
<!--
<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>
-->

<style>
#app {
  font-family: Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #000000; /* Black text color for better contrast */
  background-color: #f2f2f2; /* Light gray background color */
  margin-top: 60px;
}
</style>