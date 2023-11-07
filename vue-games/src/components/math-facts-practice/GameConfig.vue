<template>
  <div class="container">
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
      <div class="col-md-6 offset-md-3">
        <ol class="list list-numbered fs-5">
          <li class="list-item">Select an Opation</li>
          <li class="list-item">Press <span class="fw-bold">Play!</span></li>
          <li class="list-item">How many problems can you solve in 30 seconds?</li>
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