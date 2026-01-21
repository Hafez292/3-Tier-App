<template>
  <div id="app">
    <h1>{{ message }}</h1>
    <button @click="fetchData">Fetch Backend</button>
    <p>{{ apiMessage }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: 'Hello from Vue!',
      apiMessage: ''
    };
  },
  methods: {
    fetchData() {
      fetch(`${process.env.VUE_APP_API_URL}/`)
        .then(response => response.json())
        .then(data => {
          this.apiMessage = data.message;
        })
        .catch(err => {
          this.apiMessage = 'Error connecting to backend';
        });
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  margin-top: 60px;
}
</style>
