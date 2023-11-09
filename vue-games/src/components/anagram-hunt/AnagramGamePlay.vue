<template>
  <div class="container">
    <div class="row">
      <div class="col-12 d-flex align-items-center justify-content-center">
        <div class="pe-4 border-bottom pb-2">
          <span class="fs-4">Score: {{ score }}</span>
        </div>
        <div class="border-bottom pb-2">
          <span class="fs-4">Time Left: {{ timeLeft }}</span>
        </div>
      </div>
    </div>
    <div class="row mb-2">
      <div class="col-12 d-flex flex-column align-items-center justify-content-center">
        <div class="pt-2">
          <p class="fs-1">
            {{ currentWord }} ({{ currentAnagrams.length }} left)
          </p>
        </div>
        <div>
          <label for="anagram-input" class="visually-hidden">Type Here:</label>
          <input 
            v-model="userInput"
            @keyup.enter="checkAnswer"
            type="text" 
            id="anagram-input"
            class="text-center"
            name="anagram-input"
            placeholder="type here"
          >
        </div>
      </div>
    </div>
    <div class="row mt-2 mb-5">
      <div class="col-12 d-flex flex-column align-items-center justify-content-center">
        <ol>
          <li
            v-for="anagram in guessedAnagrams"
            :key="anagram"
            class="list-item"
          >
            {{ anagram }}
          </li>
        </ol>
      </div>
    </div>
  </div>
</template>

<script>

  export default {
    name: 'AnagramGamePlay',
    props: {
      wordLength: Number,
      anagramsToGuess: Array,
    },
    computed: {
      clonedAnagramsToGuess() {
        // Create a new array with cloned subarrays
        return this.anagramsToGuess.map(subArray => [...subArray]);
      },
    },
    data() {
      return {
        totalWords: 0,
        selectedAnagrams: [],
        currentWord: '',
        currentAnagrams: [],
        guessedAnagrams: [],
        userInput: '',
        score: 0,
        timeLeft: 60,
        timer: null,
      };
    },
    methods: {
      startGame() {
        
        this.selectedAnagrams = this.shuffleArray(this.clonedAnagramsToGuess);
        
        this.currentAnagrams = this.selectedAnagrams.shift();

        this.currentWord = this.currentAnagrams.shift();
        
        this.timer = setInterval(this.updateTimer, 1000);

        this.totalWords = this.selectedAnagrams.reduce((acc, arr) => acc.concat(arr), []).length;
      },
      shuffleArray(arr) {
        // Fisher-Yates (Knuth) Shuffle algorithm
        for (let i = arr.length - 1; i > 0; i--) {
          const j = Math.floor(Math.random() * (i + 1));
          [arr[i], arr[j]] = [arr[j], arr[i]];
        }
        return arr;
      },
      endGame() {
        clearInterval(this.timer);
        this.$emit('end-game');
      },
      updateTimer() {
        if (this.timeLeft > 0) {
          this.timeLeft--;
        } else {
          clearInterval(this.timer);
          this.endGame(); 
        }
      },
      fetchNewAnagrams() {
        if (this.selectedAnagrams.length === 0) {
          this.selectedAnagrams = [];
          this.recordScore();
          this.endGame();
        } else if (this.currentAnagrams.length === 0) {
          this.currentAnagrams = this.selectedAnagrams.shift();
          this.currentWord = this.currentAnagrams.shift();
        }
      },
      checkAnswer() {
        const lowerCaseInput = this.userInput.toLowerCase().trim();

        if (this.currentAnagrams.includes(lowerCaseInput)) {
          this.score += 3;
          this.$emit('update-score', this.score);

          this.currentAnagrams = this.currentAnagrams.filter(anagram => anagram !== lowerCaseInput);

          this.guessedAnagrams.push(lowerCaseInput);
          this.userInput = '';
          if (this.currentAnagrams.length === 0) {
            this.fetchNewAnagrams();
          }
        }
      },
      async recordScore() {
        const data = {
          'score': this.score,
          'word_length': this.wordLength,
          'total_words': this.totalWords,
          'game': 'ANAGRAM'
        };
        
        const response = (await this.axios.post('/games/record-score/', data)).data;
        
        console.log(response);
      },
    },
    mounted() {
      this.startGame();
    },
    watch: {
      timeLeft(newTimeLeft) {
        if (newTimeLeft === 0) {
          this.recordScore();
        }
      }
    },
  }
</script>

