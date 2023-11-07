<template>
  <div class="col-md-6">

    <h1 class="mb-0">Happy Gamers Say...</h1>
      <div id="quotes-carousel" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
          <div class="carousel-item active">
            <blockquote class="text-center py-3 fs-4 mb-0">
              <q>
                Thank you for taking the time to explore our games. We hope you enjoy your experience today!
              </q>
              <p class="fw-bold text-uppercase pt-2">
                Play2Learn Team
              </p>
            </blockquote>
          </div>
          <div v-for="(review, index) in gameReviews" :key="index" class="carousel-item">
            <blockquote class="text-center py-4 fs-4 mb-0">
              <q>
                {{ review.review }}
              </q>
              <p class="fw-bold text-uppercase pt-2">
                {{ review.username }}
              </p>
            </blockquote>
          </div>
        </div>
      </div>

  </div> 
  
  <div class="col-md-6">
    <div class="card border-0 rounded-2">
      <img src="../../../static/images/gamers_say.jpeg" alt="Gamer at Computer" class="rounded-3">
    </div>
  </div>

</template>

<script>

  export default {
    name: 'ClientQuotes',
    data() {
      return {
        gameReviews: [],
      };
    },
    mounted() {
      this.axios.get('reviews/get-game-reviews/')
      .then((response) => {
        this.gameReviews = JSON.parse(response.data.game_reviews);
      })
      .catch((error) => {
        console.error('Error fetching reviews:', error);
      });
    },
  };

</script>
