<template>
  <div class="container">

    <h1 id="game-heading" class="row-5 justify-content-center text-center mt-4">Math Practice</h1>

    <router-view></router-view>

  </div>
</template>

<script>

export default {
  name: 'MathFactsView',
}
</script>

<style scoped>

#main-container {
  margin: auto;
  width: 380px;
}


</style>