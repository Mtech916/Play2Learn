<template>
  <div id="about-container" class="container mt-4 position-relative">
    <div class="row">
      <div class="col-10 offset-1">
        <div class="d-flex flex-column align-items-center justify-content-center position-relative text-white">
          <h1 class="text-white mt-2">About us</h1>
          <p class="about-text fw-bold lh-lg">
            Play2Learn is your gateway to an exciting world of interactive learning through video games. We've reimagined education, blending the thrill of gaming with the enrichment of knowledge. Step into a universe where learning feels like playing, and every level conquered brings you closer to mastering new skills. Our mission is to make education not just informative, but incredibly fun!
          </p>
          <p class="about-text fw-bold lh-lg">
            At Play2Learn, we believe that learning is most effective when it's enjoyable, and that's why we've harnessed the power of video games to spark your curiosity. Explore a variety of games designed to teach, challenge, and inspire. Get ready to embark on an educational adventure that feels more like a thrilling quest. Join us and experience the magic of learning through play at Play2Learn!
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'AboutView',
  }
</script>

<style scoped>

/* About Page */
#about-container {
  margin-bottom: 75px;
}

.about-text {
  text-indent: 50px;
}

/* Background Image */
#about-container {
  background: url('../../../static/images/computer_gaming.jpg') center center no-repeat;
  background-size: cover;
  border-radius: 10px;
}

#about-container::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border-radius: 10px;
  background: rgba(0, 0, 0, 0.6);
}

#about-container p,
#about-container h5,
#about-container h1 {
  z-index: 10;
}

</style>