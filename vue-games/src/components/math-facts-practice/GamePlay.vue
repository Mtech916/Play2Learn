<template>

  <!-- Results -->
  <transition name="slide">
    <template v-if="timeLeft === 0">
      <div id="results-container" class="container">
        <div class="row text-center">
          <h2>Time's Up!</h2>
          <strong class="big">You Answered</strong>
          <div class="huge">{{ score }}</div>
          <strong class="big">Questions Correctly</strong>
        </div>
        <div class="d-flex flex-column justify-content-center align-items-center">
          <div class="d-grid">
            <button 
              class="btn btn--raised btn-outline-light rounded-3 form-control m-1"
              @click="restart()">
                Play Again 
            </button>
          </div>
          <div class="d-grid">
            <button 
              class="btn btn-secondary rounded-3 form-control m-1"
              @click="config()">
                Change Settings
            </button>
          </div>
        </div>
      </div>
    </template>
  </transition>

<!-- Play Game -->
  <transition name="slide-right">
    <template v-if="timeLeft > 0">
      <div id="play-container" class="container">
        <div class="row border-bottom" id="scoreboard">
            <GameScore :score="score" />
            <GameTimer :timeLeft="timeLeft" />
        </div>

        <div class="row">
            <div :class="equationClass" id="equation">
              <GameEquation 
                  :question="question"
                  :answer="+input"
                  :answered="answered"
                />
            </div>
        </div>
        <div class="row ms-2" id="buttons">
          <div class="col-md-6 offset-md-3">
            <button 
              class="btn btn-primary number-button"
              v-for="button in buttons" 
              :key="button"
              @click="setInput(button)"
            >
            {{ button }}</button>
            <button 
              class="btn btn-primary" 
              id="clear-button"
              @click="clear"
            >
            Clear</button>
          </div>
        </div>
      </div>
    </template>
  </transition>
</template>
  
<script>

  import GameScore from './GameScore.vue';
  import GameTimer from './GameTimer.vue';
  import GameEquation from './GameEquation.vue';

  import { randInt } from '../../helpers/helpers';
  
  export default {
    name: "GamePlay",
    components: {
      GameScore,
      GameTimer,
      GameEquation,
    },
    data() {
      return {
        buttons: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
        input: '',
        operands: { num1: '1', num2: '1' },
        answered: false,
        score: 0,
        gameLength: 30,
        timeLeft: 0,
      };
    },
    props: {
      operation: String,
      maxNumber: String,
    },
    methods: {
    config() {
      this.$router.push('/games/math-facts/');
    },
    setInput(value) {
      this.input += String(value);
      this.input = String(Number(this.input));
      this.answered = this.checkAnswer(
        this.input,
        this.operation,
        this.operands
      );
      if (this.answered) {
        setTimeout(this.newQuestion, 300);
        this.score++;
      }
    },
    clear() {
      this.input = '';
    },
    getRandNumbers(operator, low, high) {
      let num1 = randInt(low, high);
      let num2 = randInt(low, high);
      const numHigh = Math.max(num1, num2);
      const numLow = Math.min(num1, num2);

      if(operator === '-') {
        // Make sure higher num comes first
        num1 = numHigh;
        num2 = numLow;
      }

      if (operator === '/') { 
        if(num2 === 0) {
          // No division by zero
          num2 = randInt(1, high);
        }
        num1 = (num1 * num2);
      }
        return {num1, num2};
      },
      checkAnswer(userAnswer, operation, operands) {
        if (isNaN(userAnswer)) return false; // User hasn't answered

        let correctAnswer;
        switch(operation) {
          case '+':
            correctAnswer = operands.num1 + operands.num2;
            break;
          case '-':
            correctAnswer = operands.num1 - operands.num2;
            break;
          case 'x':
            correctAnswer = operands.num1 * operands.num2;
            break;
          default: // division
            correctAnswer = operands.num1 / operands.num2;
        }
          return (parseInt(userAnswer) === correctAnswer);
      },
      newQuestion() {
        this.input= '';
        this.answered= false;
        this.operands = this.getRandNumbers(this.operation, 0, this.maxNumber);
      },
      startTimer() {
        window.addEventListener('keyup', this.handleKeyUp);

        this.timeLeft = this.gameLength;
        if (this.timeLeft > 0) {
          this.timer = setInterval(() => {
            this.timeLeft--;
            if (this.timeLeft === 0) {
              clearInterval(this.timer);
              window.removeEventListener('keyup', this.handleKeyUp);
            }
          }, 1000);
        }
      },
      restart() {
        this.score = 0;
        this.startTimer();
        this.newQuestion();
      },
      handleKeyUp(e) {
        e.preventDefault(); // prevent the normal behavior of the key
        if (e.keyCode === 32 || e.keyCode === 13) {
          // space/Enter
          this.clear();
        } else if (e.keyCode === 8) {
          // backspace
          this.input = this.input.substring(0, this.input.length - 1);
        } else if (!isNaN(e.key)) {
          this.setInput(e.key);
        }
      },
      async recordScore() {
        const data = {
          'score': this.score,
          'operation': this.operation,
          'max_number': this.maxNumber,
          'game': 'MATH'
        };
        
        const response = (await this.axios.post('/games/record-score/', data)).data;
        
        console.log(response);
      },
    },
    mounted() {
      this.newQuestion();
      this.startTimer();
    },
    computed: {
      question() {
        const num1 = this.operands.num1;
        const num2 = this.operands.num2;
        const equation = `${num1} ${this.operation} ${num2}`;
        return equation;
        },
      equationClass() {
        if (this.answered) {
          return 'row text-primary my-2 fade';
        } else {
          return 'row text-secondary my-2';
        }
      },
    },
    watch: {
      timeLeft(newTimeLeft) {
        if (newTimeLeft === 0) {
          this.recordScore();
        }
      }
    },
  };
  
</script>

<style scoped>

/* Containers */
#results-container,
#play-container {
  margin-bottom: 75px;
}

/* button sytels */
  button.number-button {
    background-color: var(--primary);
    border-radius: .25em;
    font-size: 2.3em;
    height: 1.5em;
    margin: .1em;
    text-align: center;
    width: 25%;
  }

  #clear-button {
    background-color: var(--primary);
    border-radius: .25em;
    font-size: 2.3em;
    height: 1.5em;
    margin: .1em;
    text-align: center;
    width: 52%;
  }

/* Time's Up sytels */

  .big {
    font-size: 1.5em;
  }

  .huge {
    font-size: 5em;
  }

/* Time's Up Transitions */
  .slide-leave-active,
  .slide-enter-active {
    position: absolute;
    top: 150px;
    transition: 1s;
    width: 460px;
  }
  .slide-enter-from {
    transform: translate(-100%, 0);
    transition: opacity .5s;
  }
  .slide-leave-to {
    transform: translate(100%, 0);
    opacity:0;
  }
  .slide-right-leave-active,
  .slide-right-enter-active {
    position: absolute;
    top: 150px;
    transition: 1s;
    width: 460px;
  }
  .slide-right-enter-from {
    transform: translate(100%, 0);
    transition: opacity .5s;
  }
  .slide-right-leave-to {
    transform: translate(-100%, 0);
    opacity:0;
  }
</style>