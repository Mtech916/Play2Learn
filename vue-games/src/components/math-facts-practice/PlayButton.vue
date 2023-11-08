<template>
    <button 
      class="btn btn--raised btn-outline-light rounded-3 fs-5"
      @click="$emit('play-button-click')"
    >
    Play!</button>
</template>

<script>

export default {
  name: 'PlayButton',
}

</script>
