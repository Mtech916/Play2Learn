<template>
  <div class="col-md-6 mb-0">
      <div v-if="dataLoaded">
        <div id="quotes-carousel" class="carousel slide" data-bs-ride="carousel">
          <div class="carousel-inner">
            <div v-for="(review, index) in gameReviews" :key="index" class="carousel-item active">
              <blockquote class="d-block w-100 text-center py-4 fs-4 rounded-3 bg--quotes">
                <q>{{ review.review }}</q>
                <p class="fw-bold text-muted text-uppercase pt-2 q-name">{{ review.username }}</p>
              </blockquote>
            </div>      
          </div>
        </div>
      </div>
      <div v-else>
        <h1>
          Reviews Loading...
        </h1>
      </div>
    </div>  

</template>

<script>

  export default {
    name: 'ClientQuotes',
    data() {
      return {
        gameReviews: [],
        dataLoaded: false,
      };
    },
    mounted() {
      this.axios.get('reviews/get-game-reviews/')
      .then((response) => {
        this.gameReviews = JSON.parse(response.data.game_reviews);
        this.dataLoaded = true;
      })
      .catch((error) => {
        console.error('Error fetching reviews:', error);
        this.dataLoaded = true;
      });
    },
  };

</script>
