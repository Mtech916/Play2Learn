<template>
  <div id="anagram-config" class="container">
    <div class="row"> 
      <div class="col-sm-6 offset-sm-3">
        <label for="word-length" class="pe-2">Word Length</label>
        <input 
          type="number" 
          id="word-length" 
          v-model="wordLength"
          name="word-length" 
          placeholder="ex. 3"
          >
      </div>

    </div>
      <div class="row">
        <div class="col-12 col-md-6 offset-md-3 mt-3">
          <ol>
            <li>Choose Word Length.</li>
            <li>Press Play!</li>
            <li><span class="fs-5 fw-bold text-primary">60</span> seconds on the Clock</li>
            <li>Score <span class="fs-5 fw-bold text-success">3</span> points per correct answer</li>
            <li>Highest Scores earn <span class="fw-semibold fs-5">LeaderBoard</span> status</li>
          </ol>
        </div>
        <div class="row">
          <div class="col-12 d-flex flex-column align-items-center justify-content-center">
            <button 
              class="btn btn--raised btn-outline-light rounded-3 fs-5"
              @click='play'>
              Play!
            </button>
          </div>
        </div>
      </div>
  </div>
</template>

<script>
  export default {
    name: 'AnagramConfig',
    data() {
      return {
        wordLength: null,
      };
    },
    methods: {
      play() {
        if (this.wordLength && this.wordLength > 0) {
          this.$emit('start-game', this.wordLength);
        }
      }
    }
  }
</script>

<style scoped>

#anagram-config {
  margin-bottom: 80px;
}

</style>