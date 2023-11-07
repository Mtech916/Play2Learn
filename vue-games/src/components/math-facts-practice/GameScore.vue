<template>
  <div class="col-6 d-flex justify-content-center pe-4">
    <strong>
      <span class="fs-4">Score:</span> <span class="text-success fs-3">{{ score }}</span>
    </strong>  
  </div>
</template>

<script>

export default {
  name: 'GameScore',
  props: {
    score: Number
  }
}

</script>