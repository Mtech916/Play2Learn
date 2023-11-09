<template>
  <div class="row">
    <div class="d-flex flex-column justify-content-center align-items-center text-center my-4">
      <h5 class="badge bg-primary">
        Word <i class="fa-solid fa-puzzle-piece"></i>
      </h5>
      <h1>Anagram Hunt</h1>
    </div>
  </div>

  <AnagramConfig v-if="!gameStarted" @start-game="startGame" />
  <AnagramGamePlay v-else-if="gameStarted && !gameOver" :wordLength="wordLength" @end-game="onEndGame" @update-score="updateScore"/>
  <AnagramGameOver v-else :score="score" @restart-game="restartGame" @back-to-config="backToConfig" />

</template>

<script>

import AnagramConfig from '../components/anagram-hunt/AnagramConfig.vue';
import AnagramGamePlay from '../components/anagram-hunt/AnagramGamePlay.vue';
import AnagramGameOver from '../components/anagram-hunt/AnagramGameOver.vue';

import anagrams from '../data/anagrams.js';

  export default {
    name: 'AnagramHunt',
    components: {
      AnagramConfig,
      AnagramGamePlay,
      AnagramGameOver
    },
    data() {
      return {
        gameStarted: false,
        gameOver: false,
        wordLength: null,
        selectedAnagrams: [],
        score: 0,
      }
    },
    methods: {
      startGame(wordLength) {
        this.wordLength = wordLength;
        this.gameStarted = true;
      },
      updateScore(newScore) {
        this.score = newScore;
      },
      onEndGame() {
      this.gameOver = true;
      },
      restartGame() {
        this.score = 0;
        this.selectedAnagrams = [...anagrams[this.wordLength]];
        this.gameStarted = true;
        this.gameOver = false;
      },
      backToConfig() {
        this.wordLength = null;
        this.score = 0;
        this.gameStarted = false;
        this.gameOver = false;
      },
    }
  }
</script>


<style scoped>

h5.badge {
  font-size: 1.1rem;
}

</style>