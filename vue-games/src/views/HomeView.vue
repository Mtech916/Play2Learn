<template>
  <main id="home-view">
    <div class="container-fluid">
      <h1 class="d-flex flex-start text--lg py-5">Happy Clients Say...</h1>

      <div class="row">
        <ClientQuotes />
  
        <AvailableGames />
      </div>
      <div class="row">
        <h2 class="text-center">coming soon!</h2>
      </div>

    </div>
  </main>

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