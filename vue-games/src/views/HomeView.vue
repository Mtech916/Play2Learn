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
        <h3 class="text-center --ltr-spc">Questions or requests please email us <i class="fa-solid fa-arrow-down"></i></h3>
      </div>
    </div>
</template>

<script>

  import ClientQuotes from '../components/ClientQuotes.vue';
  import AvailableGames from '../components/AvailableGames.vue';

  export default {
    name: 'HomeView',
    components: {
      ClientQuotes,
      AvailableGames
    },
  }

</script>

<style scoped>

.--ltr-spc {
  letter-spacing: .015em;
}

/* Home page background */
.available-games {
  background: url('../../public/images/cool_bg.jpg') center center no-repeat;
  background-size: cover;
  background-attachment: fixed;
}

.available-games::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.7);
}


@media (max-width: 760px) {
  #home-view {
    margin-bottom: 70px;
  }
}

</style>