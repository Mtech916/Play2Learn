<template>
  <div class="container funky-bg position-relative">
    <div class="row">
      <div class="col-md-6 mt-5">
          <div class="image-container d-flex justify-content-center align-items-center">
            <img src="../../../static/images/Anagram-Hunt-thumbnail.png" alt="Anagram Hunt Thumbnail" class="rounded-3" />
          </div>
      </div>
      
      <div class="col-md-6 mt-3 my-md-5">
        <h5 class="d-flex justify-content-center align-items-center">Hunt your mind and rearrange the letters to create different words. How many can you guess in 60 seconds?</h5>
        <div class="row">
          <div class="col-6 offset-3">
            <div class="d-grid">
              <a href="/games/anagram-hunt/" class="btn btn--raised">Play</a>
            </div>
          </div>
        </div>
      </div>
      
      <div class="row mb-5">
        <div class="col-md-6 mt-5">
          <div class="image-container d-flex justify-content-center align-items-center">
            <img src="../../../static/images/Math-Facts-thumbnail.png" alt="Math Facts Thumbnail" class="rounded-3" />
          </div>
        </div>
        <div class="col-md-6 mt-3 my-md-5">
          <h5 class="d-flex justify-content-center align-items-center">
            You think your fast? ...well you only have 30 seconds, better make'em count. P.S. The math pun was for free!
          </h5>
          <div class="row">
            <div class="col-6 offset-3">
              <div class="d-grid">
                <a href="/games/math-facts/" class="btn btn--raised">Play</a>
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
