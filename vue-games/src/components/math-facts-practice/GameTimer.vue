<template>
  <div class="col-6 d-flex justify-content-center">
    <strong>
      <span class="fs-4">Time:</span> <span class="fs-5">{{ timeLeft }}</span>
    </strong>  
  </div>
</template>

<script>

export default {
  name: 'GameTimer',
  props: {
    timeLeft: Number,
  }
}

</script>