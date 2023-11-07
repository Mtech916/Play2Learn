<template>
  <div id="equation" class="col-md-6 offset-md-3 text-center fs-4">
    <div class="">
      {{ question }} = {{ answer }}
    </div>
  </div>
</template>

<script>

export default {
  name: 'GameEquation',
  props: {
    question: String,
    answer: Number,
    answered: Boolean
  }
}

</script>

<style scoped>

  /* #equation {
    font-size: 1.6em;
    margin: auto;
    width: 90%;
  } */

</style>