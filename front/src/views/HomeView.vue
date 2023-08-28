<template>
  <div class="w-100 h-100 px-3 pt-2 pb-5  d-flex flex-column  bg--warning align-self-center justify-center">
    <div class="row ">
      <div class="col-12 col-sm-8 col-md-6 col-lg-5 col-xl-3 m-auto">
        <div class="card shadow-lg p-3 text-center">
          <div class="text-center">
            <img class="logo mb-3" src="../assets/logo2.png" alt="">
          </div>
          <h3><b>КЕНГУРУ МАРКЕТ</b></h3>


          <form class="card-body text-center" v-if="isLoad==='ok'">


            <div class="mb-5">
              <v-autocomplete
                  label="Маркет*"
                  item-text="name"
                  no-data-text="Маркет не найден"
                  item-value="id"
                  :messages="`Был: ` + lastMarket"
                  :items="marketsList"
                  v-model="market"/>
            </div>

            <div class="mb-5">

              <v-autocomplete
                  label="Аудиоустройство*"
                  v-model="audio"
                  item-text="name"
                  :messages="`Было: ` + lastAudio"
                  item-value="id"
                  no-data-text="Не найдены аудиоустройства"
                  :items="audioList"
              ></v-autocomplete>

            </div>

            <div class="mb-5 mt-5">
              <small>Синхронизация: {{ dateUpdate }}</small>
            </div>


            <v-btn
                color="warning"
                dark
                class="px-5"
                @click="save"
                :disabled="!(market && audio) "
            >Синхронизировать
            </v-btn>


          </form>
          <div class="card-body text-center" v-if="isLoad==='error'">
            <div class="mb-3">{{ errorText }}</div>
            <v-btn
                color="warning"
                dark
                class="px-5"
                @click="refresh"
            >Обновить
            </v-btn>


          </div>

          <div class="card-body text-center" v-if="isLoad===''">
            <p>Загрузка...</p>


          </div>

        </div>
      </div>
    </div>

  </div>

</template>

<script>


import LOCAL_CONFIG from "@/LOCAL_CONFIG";
import CookieHelper from "@/plugins/cookieHelper";

export default {
  name: "HomeView",
  components: {},
  data() {
    return {
      market: '',
      audio: '',
      lastAudio: 'н/д',
      lastMarket: 'н/д',
      errorText: '',
      dateUpdate: 'н/д',
      marketsList: [],
      audioList: [],
      isLoad: ''
    }
  },

  created: async function () {
    this.refresh()
  },

  methods: {
    async getMarket() {

      const self = this;
      self.marketsList = [];

      try {
        const url = LOCAL_CONFIG.urls.autocomplete;
        const response = await fetch(url, {
          method: 'POST',
          body: JSON.stringify({
            token: LOCAL_CONFIG.marketToken
          }),
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': CookieHelper.getCookie('csrftoken')
          },
        });
        if (response.status === 200) {
          self.marketsList = await response.json();
        } else {
          self.isLoad = 'error'
          this.$emit('showAlert', 'Ошибка  при обращение к CRM. Подробности в консоли');
          self.errorText = 'Ошибка при обращение к CRM. Подробности в консоли';
        }
      } catch (e) {
        self.isLoad = 'error'
        this.$emit('showAlert', "Ошибка при обращение к CRM. Подробности в консоли");
        self.errorText = 'Ошибка при обращение к CRM. Подробности в консоли';
      }

    },

    async getLocalSetting() {

      const self = this;

      try {
        const url = LOCAL_CONFIG.urls.localSetting;
        const response = await fetch(url, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': CookieHelper.getCookie('csrftoken')
          },
        });
        if (response.status === 200) {
          const data = await response.json();
          self.audioList = data.audioList;
          self.market = data.setting.marketId;
          self.lastMarket = data.setting.marketName;
          self.lastAudio = data.setting.audio;
          self.audio = data.setting.audio;
          self.dateUpdate = data.setting.dateUpdate;
          self.isLoad = 'ok'
        } else {
          self.isLoad = 'error'
          this.$emit('showAlert', 'Ошибка  при обращение к настройкам клиента. Подробности в консоли');
          self.errorText = 'Ошибка при обращение к настройкам клиента. Подробности в консоли';
        }
      } catch (e) {
        self.isLoad = 'error'
        this.$emit('showAlert', "Ошибка  при обращение к настройкам клиента. Подробности в консоли");
        self.errorText = 'Ошибка при обращение к настройкам клиента. Подробности в консоли';
      }

    },

    async refresh() {
      this.isLoad = '';
      await this.getMarket();
      if (this.marketsList) {
        await this.getLocalSetting();
      }

    },

    async save() {
      try {
        const index = this.marketsList.findIndex(p => p.id === this.market);
        const marketName = this.marketsList[index].name;
        this.isLoad = '';

        const url = LOCAL_CONFIG.urls.localSetting;
        const response = await fetch(url, {
          method: 'POST',
          body: JSON.stringify({
            'marketId': this.market,
            'marketName': marketName,
            'audio': this.audio,

          }),
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': CookieHelper.getCookie('csrftoken')
          },
        });
        if (response.status === 200) {
          this.$emit('showAlert', 'Синхронизация с CRM прошла');
          this.refresh()
        } else {
          this.$emit('showAlert', 'Ошибка при синхронизации. Подробности в консоли');
        }
      } catch (e) {
        this.$emit('showAlert', "Ошибка при синхронизации. Подробности в консоли");
      }

           this.isLoad = 'ok';
    }
  },


}
</script>

<style scoped lang="scss">

.tab-content {
  border: #dee2e6 1px solid;
}

.logo {
  width: 100px;
}

.logo-as {
  height: 70px;

}
</style>