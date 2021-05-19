<template>
  <div class="">

      <div class="col-md-12 mb-5" v-if="createNew">
        <CreateVideo v-on:createdVideo="updatedVideos" />
      </div>      
    <div class="row">
        <div class="col-md-5 text-center nincefont">
            <h4>Welcome to Youtube Rater</h4>
                <form @submit="createdNew()">
                    <input class="btn-sm btn-primary mb-3 btn-center" id="createdNew" type="submit" value="Create new video">
                </form>  
            <!--<button v-on:click="getVideos">Get my first Videos</button>
            {{ videos[0].description }} -->

            <p v-bind:key="video.id" v-for="video in videos">
                {{ video.title }}
                <br>
                Rating: {{ video.rating_average }}
                <br>
                Comment: {{ video.comments_list[0] }}
                <br>
                <button class="btn-sm btn-primary mt-2 mb-3" v-on:click="videoDetail(video)" >Details</button>
            </p>
        </div>
        <div class="col-md-6">
            <VideoDetails v-bind:videodetail="videodetail" v-on:updatedVideo="updatedVideos" v-on:deletedVideo="updatedVideos"/>
        </div>
    </div>

  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios';
import VideoDetails from './VideoDetails';
import CreateVideo from './CreateVideo';

export default {
  name: 'home',
  components: {
    VideoDetails,
    CreateVideo,
  },
  data() {
      return {
          videos: [],
          videodetail: Object,
          createNew: "",
      }      
  },
  methods: {
      
      getVideos() {
          axios.get("http://127.0.0.1:8000/api/videos/")
          .then(res => (this.videos = res.data))                 //console.log(res.data)
          .catch(err => console.log(err));
      },
      videoDetail(video) {
          this.videodetail = video;
          console.log(this.videodetail)
      },
      createdNew() {
          this.createNew = !this.createNew;
      },
      updatedVideos() {
          this.timer = setTimeout(() => 
            axios.get("http://127.0.0.1:8000/api/videos/")
            .then(res => {
                console.log(res.data)
                this.videos = res.data
            })
            .catch(err => {
                console.error(err); 
          }), 600);
      }
      
  },
  created() {
      this.getVideos();
      createNew: false;
  },
}

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Alatsi&display=swap');

.nincefont {
    font-size: 26px;
    font-family: 'Alatsi', sans-serif;
}
</style>