<template>
  <div id="game-config" class="container">
    <div class="row">
      <div class="col-md-6 offset-md-3">
        <SelectInput 
            :currentValue="operation" 
            label="Operation" id="operation"  
            v-model="operation" 
            :options="operations"
            @input="(o) => (this.operation = o)" 
          />
        <SelectInput 
            :currentValue="maxNumber" 
            label="Maximum Number" 
            id="max-number" 
            v-model="maxNumber" 
            :options="numbers" 
            @input="(n) => (this.maxNumber = n)"
          />
      </div>
    </div>
    <div class="row">
      <div class="col-12 col-md-6 offset-md-3">
        <ol class="">
          <li>Select an Operation</li>
          <li>Press <span class="fw-bold">Play!</span></li>
          <li>30 seconds on the Clock</li>
          <li>Score 1 point per correct answer</li>
          <li>Highest Scores make it to the <span class="success">LeaderBoard</span></li>
        </ol>
      </div>
    </div>
    <div class="row">
      <div class="col-6 offset-3">
        <PlayButton @play-button-click="play"/>
      </div>
    </div>
  </div>
</template>

<script>

import SelectInput from './SelectInput.vue';
import PlayButton from './PlayButton.vue';

export default {
  name: "GameConfig",
  components: {
    SelectInput,
    PlayButton,
  },
  data() {
    return {
      operations: [
        ['Addition', '+'],
        ['Subtraction', '-'],
        ['Multiplication', 'x'],
        ['Division', '/']
      ],
      operation: '+',
      maxNumber: '10',
    };
  },
  methods: {
    play() {
      this.$router.push({
        path: '/math-facts/play',
        name: 'GamePlay',
        query: {
          operation: this.operation,
          maxNumber: this.maxNumber,
        },
      });
    },
  },
  computed: {
    numbers() {
      const numbers = [];
      for (let number = 2; number <= 100; number++) {
        numbers.push([number, number]);
      }
        return numbers;
    },
  },
};

</script>

<style scoped>

#game-config {
  margin-bottom: 75px;
}

</style>