<template>
  <div id="app">
    <div class="row justify-between navbar">
      <img src="@/assets/logo.svg" alt="logo">
      <img src="@/assets/burger.svg" alt="menu toggle">
    </div>
    <div class="map">
      <HereMap
        :apikey="apikey"
        lat="52.51"
        lng="13.4"
        width="100%"
        height="calc(100vh - 62px)"
        :dataPoints="dataPoints"
      />
      <div class="places">
        <div class="row">
          <div :id="`div-${item.position.lat}`" v-for="(item, index) in dataPoints" :key="index" class="place">
            <div class="row">
              <img class="place-img" src="@/assets/hotel.jpg" alt="hotel" width="50%">
              <div class="place-detail">
                <p class="title">{{ item.title }}</p>
                <p class="dist uppercase">3.4 KM from city center</p>
                <p class="price">£{{ item.price }}</p>
                <p class="dist">Designs may vary</p>
              </div>
            </div>
            <button class="btn-book">Book</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable no-undef */
import axios from 'axios'
import HereMap from '@/components/HereMap.vue'

export default {
  name: 'App',
  components: {
    HereMap
  },
  data () {
    return {
      apikey: '7UHRoiZWSxEwiAcIlTd-EZKDkEAM6xbgMdYhNOVWym4',
      dataPoints: [],
      places: []
    }
  },
  created () {
    this.getPlaces()
  },
  methods: {
    async getPlaces () {
      try {
        const { data } = await axios.get('https://curassessment.herokuapp.com/api/properties/?at=52.51,13.4')
        this.dataPoints = data
      } catch (error) {
        console.log(error)
      }
    }
  }
}
</script>

<style lang="scss">
@import '@/assets/styles/main.scss';

.navbar {
  padding: 20px;
}

.map {
  position: relative;

  .places {
    position: absolute;
    bottom: 20px;
    overflow-x: scroll;
    width: 100%;
    -ms-overflow-style: none;
    scrollbar-width: none;

    .places::-webkit-scrollbar {
      display: none;
    }
  }

  .place {
    min-width: 300px;
    min-height: 250px;
    background-color: #ffffff;
    padding: 10px;
    margin: 0 20px;

    .place-img {
      object-fit: cover;
      height: 280px;
    }

    .place-detail {
      padding: 10px;
    }

    .title {
      font-size: 18px;
      font-weight: bold;
    }

    .dist {
      color: #767676;
      font-weight: 14px;
    }

    .price {
      font-size: 24px;
      font-weight: bold;
    }

    .btn-book {
      background-color: #F39431;
      color: #ffffff;
      border: none;
      outline: none;
      padding: 15px;
      width: 100%;
      margin-top: 15px;
      font-size: 20px;
    }
  }
}
</style>
