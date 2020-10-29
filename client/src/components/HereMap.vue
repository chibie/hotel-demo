<template>
  <div ref="map" v-bind:style="{ width: width, height: height }"></div>
</template>

<script>
/* eslint-disable no-undef */
/* eslint-disable no-unused-vars */

export default {
  name: 'HereMap',
  props: {
    apikey: String,
    lat: String,
    lng: String,
    width: String,
    height: String,
    dataPoints: Array
  },
  data () {
    return {
      map: {},
      platform: {},
      iconType: 'default'
    }
  },
  computed: {
    icon () {
      return require(`@/assets/home-${this.iconType}.svg`)
    }
  },
  watch: {
    dataPoints (val) {
      this.initMap()
    }
  },
  created () {
    this.platform = new H.service.Platform({
      apikey: this.apikey
    })
  },
  mounted () {
    if (this.dataPoints.length) {
      this.initMap()
    }
  },
  methods: {
    initMap () {
      const defaultLayers = this.platform.createDefaultLayers()
      // Define a variable holding mark-up that defines an icon image
      const defaultImg = new Image()
      defaultImg.src = this.icon
      const imgIcon = defaultImg

      this.map = new H.Map(
        this.$refs.map,
        defaultLayers.vector.normal.map,
        {
          zoom: 15,
          center: this.dataPoints.length ? this.dataPoints[0].position : { lat: 0, lng: 0 }
        }
      )

      window.addEventListener('resize', () => this.map.getViewPort().resize())

      // Create an icon, an object holding the latitude and longitude, and a marker:
      const icon = new H.map.Icon(imgIcon)
      const group = new H.map.Group()
      this.map.addObject(group)

      group.addEventListener('tap', (evt) => {
        const element = document.getElementById(`div-${evt.target.getData().position.lat}`)
        element.scrollIntoView({ behavior: 'smooth' })
        this.iconType = 'active'
        console.log(evt.target.getData())
      }, false)

      for (let i = 0; i < this.dataPoints.length; i++) {
        this.addMarkerToGroup(this.dataPoints[i].position, icon, this.dataPoints[i], group)
      }

      // MapEvents enables the event system
      // Behavior implements default interactions for pan/zoom (also on mobile touch environments)
      var behavior = new H.mapevents.Behavior(new H.mapevents.MapEvents(this.map))

      // create default UI with layers provided by the platform
      var ui = H.ui.UI.createDefault(this.map, defaultLayers)
    },
    addMarkerToGroup (pos, icon, data, group) {
      const marker = new H.map.Marker(pos, { icon: icon })
      marker.setData(data)
      marker.addEventListener('tap', (e) => {
        // marker.setIcon()
      })
      group.addObject(marker)
    }
  }
}
</script>

<style scoped lang="scss">

</style>
