<template>
  <div id="app">
    <v-app class="w-100">

      <v-main>

        <home-view @showAlert="showAlert($event)"/>

        <v-snackbar
            color="white"
            v-model="snackbar"
        >
          <span class="text-dark">{{ snackbarText }}</span>

          <template v-slot:action="{ attrs }">
            <v-btn
                color="orange accent-2"
                tile
                v-bind="attrs"
                @click="snackbar = false"
            >
              Ок
            </v-btn>
          </template>
        </v-snackbar>

      </v-main>
    </v-app>

  </div>
</template>

<style lang="scss" src="./assets/style.scss">
</style>

<script>
import HomeView from "@/views/HomeView";


export default {


  components: {
    HomeView

  },

  methods: {

    showAlert(text) {
      this.snackbar = true
      this.snackbarText = text;
    },




  },

  data() {
    return {
      snackbar: false,
      snackbarText: ""
    }
  },


}
</script>