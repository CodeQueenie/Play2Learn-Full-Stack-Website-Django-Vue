<template>
  <div class="container funky-bg position-relative">
    <div class="row">
      <div class="col-md-6 mt-5">
          <div class="image-container d-flex justify-content-center align-items-center">
            <img src="../../public/images/wordgamepic.jpg" alt="Anagram Hunt Thumbnail" class="rounded-3" width="250"/>
          </div>
      </div>
      
      <div class="col-md-6 mt-3 my-md-5">
        <div class="d-flex flex-column justify-content-center align-items-center">
          <h5 class="badge bg-anagram">
            Anagram Hunt
          </h5>
          <p class="fw-bold">
            Dive into a world where letters twist and turn, challenging you to find words hidden in plain sight. Every solved puzzle brings you closer to the top. Are you up for the challenge?
          </p>
        </div>
        <div class="row">
          <div class="col-6 offset-3">
            <div class="d-grid">
              <a 
                href="/games/anagram-hunt/"
                class="btn btn--raised rounded-3"
              >
                Play & Compete
              </a>
            </div>
          </div>
        </div>
      </div>
      
      <div class="row mb-5">
        <div class="col-md-6 mt-5">
          <div class="image-container d-flex justify-content-center align-items-center">
            <img src="../../public/images/mathpic.jpg" alt="Math Facts Thumbnail" class="rounded-3" width="250" />
          </div>
        </div>
        <div class="col-md-6 mt-3 my-md-5">
          <div class="d-flex flex-column justify-content-center align-items-center">
            <h5 class="badge bg-math-facts">
              Math Facts
            </h5>
            <p class="fw-bold">
              Numbers have never been more fun! Tackle our challenge and boost your arithmetic skills. With each correct answer, you carve a path to victory. Ready, set, calculate!
            </p>
          </div>
          <div class="row">
            <div class="col-6 offset-3">
              <div class="d-grid">
                <a
                  href="/games/math-facts/"  
                  class="btn btn--raised rounded-3"
                > 
                  Play & Show Your Skills
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

<style scoped>
.funky-bg {
  z-index: 10;
  color: #fff;
}

/* Styling for 'Anagram Hunt' badge */
.bg-anagram {
  background-color: #808080;
  color: #fff;
  padding: 5px 10px;
  border-radius: 10px;
  margin-bottom: 10px;
  display: inline-block;
}

/* Styling for 'Math Facts' badge */
.bg-math-facts {
  background-color: #808080;
  color: #fff;
  padding: 5px 10px;
  border-radius: 10px;
  margin-bottom: 10px;
  display: inline-block;
}

/* Styling for game descriptions */
p {
  color: #333;
  font-size: 1rem;
  line-height: 1.5;
}
</style>