<template>
  <div class="container">
    <div class="row">
      <div class="col-md-6 offset-md-3">
          <div class="d-flex flex-column align-items-center justify-content-center text-center mt-3">
            <h5 class="badge bg-primary">
              + <span class="text-black">|</span> - <span class="text-black">|</span> / <span class="text-black">|</span> x
            </h5>
            <h1 id="game-heading" class="fw-bold">
              Math Practice
            </h1>
          </div>
      </div>
    </div>

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