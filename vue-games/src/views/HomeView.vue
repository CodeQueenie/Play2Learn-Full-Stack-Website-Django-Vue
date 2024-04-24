<template>
  <div class="container my-5" id="home-view">
    <header class="text-center my-4">
      <h1 class="page-title">Welcome to Our Gaming Site</h1>
    </header>

    <main>
      <section class="client-quotes my-5">
        <ClientQuotes />
      </section>

      <section class="available-games my-5">
        <AvailableGames />
      </section>
      
      <section class="contact-info text-center my-5">
        <h2>Reach Out to Us!</h2>
        <p>We're here to help with any questions or special requests.</p>
        <p>Click the <i class="fa fa-envelope" aria-hidden="true"></i> icon below to get in touch with us!</p>
      </section>
    </main>
  </div>
</template>

<script>
import ClientQuotes from '../components/ClientQuotes.vue';
import AvailableGames from '../components/AvailableGames.vue';

export default {
  name: 'HomeView',
  components: {
    ClientQuotes,
    AvailableGames
  },
}
</script>

<style scoped>
#home-view .page-title {
  font-size: 2.5em;
  margin-bottom: 0.5em;
  color: #f0f0f0; /* Ensuring text is readable against the darker background */
}

.container {
  background-color: #949aa2; /* A consistent darker background throughout */
}

.available-games::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(255, 255, 255, 0.8);
  border-radius: 8px; /* Match parent's border-radius */
  z-index: -1;
}

.available-games {
  position: relative; /* Ensure the pseudo-element positions relative to this. */
  background-image: url('../../../static/images/home.jpg');
  background-size: cover;
  background-repeat: no-repeat;
  background-attachment: fixed;
  z-index: 0; /* Ensures that content overlays the pseudo-background */
}

.fa-envelope {
  font-size: 24px;
  color: whitesmoke; /* Ensuring the icon is clearly visible */
}

#home-view {
  overflow-y: auto; /* Add scrolling capability if the content overflows */
}

@media (max-width: 760px) {
  .available-games {
    background-attachment: scroll; /* Ensuring it is mobile-friendly */
  }
}
</style>