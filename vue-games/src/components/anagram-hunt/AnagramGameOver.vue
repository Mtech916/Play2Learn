<template>
  <div id="anagram-final-results" class="container">
    <div class="row text-center mb-2">
      <h2>Time's Up!</h2>
      <strong class="big">You Got</strong>
      <div class="huge">{{ score }}</div>
      <strong class="big ">Anagrams</strong>
    </div>

    <div id="settings-container" class="d-flex flex-column justify-content-center align-items-center">
      <div class="d-grid mb-2">
        <button 
          class="btn btn--raised btn-outline-light rounded-3"
          @click="restartGame"
        >
          Play Again
        </button>
      </div>
      <div class="d-grid">
        <button 
        class="btn btn-secondary rounded-3"
        @click="backToConfig"
        >
          Change Settings
        </button>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'AnagramGameOver',
    props: {
      score: Number
    },
    methods: {
      restartGame() {
        this.$emit('restart-game');
      },
      backToConfig() {
        this.$emit('back-to-config');
      },
    },
  }
</script>

<style scoped>

/* Time's Up sytels */
.big {
    font-size: 1.5em;
  }

  .huge {
    font-size: 5em;
  }

  #settings-container {
    margin-bottom: 75px;
  }

</style>