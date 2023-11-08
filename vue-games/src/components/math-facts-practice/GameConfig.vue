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
        <ol>
          <li>Select an Operation</li>
          <li>Press Play!</li>
          <li><span class="fs-5 fw-bold text-primary">30</span> seconds on the Clock</li>
          <li>Score <span class="fs-5 fw-bold text-success">1</span> point per correct answer</li>
          <li>Highest Scores earn <span class="fw-semibold fs-5">LeaderBoard</span> status</li>
        </ol>
      </div>
    </div>
    <div class="row">
      <div class="col-12 d-flex flex-column align-items-center justify-content-center">
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