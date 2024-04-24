<template>
  <div class="col-md-6">
    <h1 class="mb-0">Brain-Powered Fun Awaits</h1>
    <div id="quotes-carousel" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <!-- Enhanced introductory message with a competitive edge -->
        <div class="carousel-item active">
          <blockquote class="text-center py-4 fs-4 mb-0">
            <p>Step into a world where words twist and numbers bend in your quest for knowledge. Challenge your mind with our Anagram Hunt and Math Game, and see where you stand on our leaderboards. Every puzzle solved, every challenge conquered, is your chance to shine among peers and puzzle enthusiasts alike. Are you ready to be crowned the sharpest mind?</p>
          </blockquote>
        </div>
        <!-- Placeholder for user reviews -->
        <div v-for="(review, index) in gameReviews" :key="index" class="carousel-item">
          <blockquote class="text-center py-4 fs-4 mb-0">
            <q>
              {{ review.review }}
            </q>
            <p class="fw-bold text-uppercase pt-2">
              <span class="carousel-username">{{ review.username }}</span>
            </p>
          </blockquote>
        </div>
      </div>
    </div>
  </div>

  <div class="col-md-6">
    <div class="card border-0 rounded-2">
      <img src="../../public/images/excitedpeople.jpg" alt="Excited People" class="rounded-3">
    </div>
  </div>
</template>

<script>
export default {
  name: 'ClientQuotes',
  data() {
    return {
      gameReviews: [],
    };
  },
  mounted() {
    this.axios.get('reviews/get-game-reviews/')
    .then((response) => {
      this.gameReviews = JSON.parse(response.data.game_reviews);
    })
    .catch((error) => {
      console.error('Error fetching reviews:', error);
    });
  },
};
</script>

<style>
.carousel-username {
    color: rgb(40, 40, 224);
}
</style>