<template>
  <div class="main-text" v-if="videodetail.title != null">
    <div class="row">
      <div class="col-md-10" >
        <p class="mb-3"><span class="bodyp">Title:</span> {{ videodetail.title }} </p>        

        <p><span class="bodyp">Description: </span>{{ videodetail.description }} </p>        

        <p>Rating: {{ videodetail.rating_average }} </p>        

        <p v-if="videodetail.comments_list.length > 0">Comments: {{ videodetail.comments_list}} </p>

        <iframe width="400" height="215" :src="videodetail.url" 
        frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope;
        picture-in-picture" allowfullscreen></iframe>

        <p>Url: {{ videodetail.url}} </p>

        <p>Category: {{ videodetail.category}} </p>
        
      </div>
    </div>

    <form action="formvideo" @submit.prevent="giveRating1" @submit="$emit('updatedVideo', videodetail)">
      <p>
        <label for="stars">Give a Rating</label>
        <input class="ml-2" type="text" name="stars" id="stars" v-model="stars">
      </p>  
      <p>
        <label for="comments">Comments</label>
        <input class="ml-2" type="text" name="comments" id="comments" v-model="comments">
      </p>
      <p>
        <input class="btn-primary" type="submit" value="Submit Rating">
      </p>
    </form>

    <button class="btn-sm btn-danger mt-2 mb-3" v-on:click="videoDelete(videodetail)" @click="$emit('deletedVideo', videodetail)">Delete Video</button>
   

  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios';
import { TokenService } from '../storage/service'

export default {
  name: 'VideoDetails',
  components: {
    
  },
  props: {
      videodetail: {}
  },
  data() {
      return {
          videos: [],
          stars: '',
          comments: '',
      }      
  },
  methods: {
    videoDelete(videodetail) {
      
      console.log(this.token);

      var postData = {
        video: this.videodetail.id,
      };

      let axiosConfig = {
        headers: {
          'Authorization': 'Token '+ this.token // For Django
        }
      };

      axios.delete(`http://127.0.0.1:8000/api/videos/${this.videodetail.id}`, axiosConfig)  // '가 아니라 `이다.
      .then(res => {
        console.log(res.data)
      })
      .catch(err => {
        console.error(err); 
      })    
    },

    giveRating1(stars, comments) {
      this.token = TokenService.getToken();

      console.log(this.videodetail.id);

      var postData = {
        stars: this.stars,
        comments: this.comments,
      };

      let axiosConfig = {
        headers: {
          'Authorization': 'Token '+ this.token // For Django
        }
      };

      axios.post(`http://127.0.0.1:8000/api/videos/${this.videodetail.id}/rate_video/`, postData, axiosConfig)
      .then(res => {
        console.log(res.data)
      })
      .catch(err => {
        console.error(err); 
      })
    }
  },
  created() {
    let token;
    this.token = TokenService.getToken();
  },

}

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Alatsi|Muli&display=swap');

.main-text {
  font-family: 'Muli', sans-serif;
  font-size: 20px;
  color: black;
}

.bodyp {
  color: blue;
  font-family: 'Muli', sans-serif;
}
</style>