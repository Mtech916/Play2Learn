<template>
  <div class="container vh-75 my-5">
    <div class="row">
      <ClientQuotes />
    </div>
  </div>
    <div class="available-games position-relative my-5">
      <AvailableGames />
    </div>
    <div class="container">
      <div class="row my-5">
        <h2 class="text-center">coming soon!</h2>
      </div>
    </div>
</template>

<script>

  import ClientQuotes from './ClientQuotes.vue';
  import AvailableGames from './AvailableGames.vue';

  export default {
    name: 'HomeView',
    components: {
      ClientQuotes,
      AvailableGames
    },
  }

</script>

<style scoped>

#home-view {
  margin-bottom: 100px;
}

@media (max-width: 760px) {
  #home-view {
    margin-bottom: 70px;
  }
}

</style>