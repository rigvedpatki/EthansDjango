<template>
  <b-container>
    <b-col align-self="center">
      <b-jumbotron header="Error 404" lead="Page not found." style="text-align: center" class="m-5">
        <p>Return back to home page.</p>
        <b-btn variant="primary" @click="$router.push('/')">Home page</b-btn>
      </b-jumbotron>
    </b-col>
  </b-container>
</template>
<script>
export default {
  name: 'Error',
  data() {
    return {}
  },
  methods: {}
}
</script>