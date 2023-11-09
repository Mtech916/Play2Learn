<template>
  <div class="container funky-bg position-relative">
    <div class="row">
      <div class="col-md-6 mt-5">
          <div class="image-container d-flex justify-content-center align-items-center">
            <img src="../../../static/images/anagram-thumbnail.png" alt="Anagram Hunt Thumbnail" class="rounded-3" width="250"/>
          </div>
      </div>
      
      <div class="col-md-6 mt-3 my-md-5">
        <div class="d-flex flex-column justify-content-center align-items-center">
          <h5 class="badge bg-primary">
            Anagram Hunt
          </h5>
          <p class="fw-bold">
            Unleash your word skills in our thrilling Anagram Hunt! Solve brain-twisting word puzzles in a race against time. Can you unscramble them all?
          </p>
        </div>
        <div class="row">
          <div class="col-6 offset-3">
            <div class="d-grid">
              <a 
                href="/games/anagram-hunt/"
                class="btn btn--raised rounded-3"
              >
                Play
              </a>
            </div>
          </div>
        </div>
      </div>
      
      <div class="row mb-5">
        <div class="col-md-6 mt-5">
          <div class="image-container d-flex justify-content-center align-items-center">
            <img src="../../../static/images/math-thumbnail.png" alt="Math Facts Thumbnail" class="rounded-3" width="250" />
          </div>
        </div>
        <div class="col-md-6 mt-3 my-md-5">
          <div class="d-flex flex-column justify-content-center align-items-center">
            <h5 class="badge bg-primary">
              Math Facts Practice
            </h5>
            <p class="fw-bold">
              Sharpen your math prowess with our Math Facts Practice game. Challenge your number skills and beat the clock. Get ready to excel
            </p>
          </div>
          <div class="row">
            <div class="col-6 offset-3">
              <div class="d-grid">
                <a
                  href="/games/math-facts/"  
                  class="btn btn--raised rounded-3"
                >
                  Play
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'AvailableGames'
  }
</script>
