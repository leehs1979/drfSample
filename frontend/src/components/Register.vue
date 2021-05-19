<template>
  <div class="">
      <h1>User Registration</h1>

      <form id="formvideo" @submit.prevent="CreateUser">
        <p>
            <label for="username">Username</label>
            <input class="ml-2" type="text" name="username" id="username" v-model="username">
        </p>
        <p>
            <label for="password">Password</label>
            <input class="ml-2" type="text" name="password" id="password" v-model="password">
        </p>          
        <p>
            <input type="submit" value="Submit">
        </p>

      </form>
   

  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios';

export default {
  name: 'register',
  components: {
    
  },
  data() {
      return {
          username: null,
          password: null,
      }      
  },
  methods: {
      
      CreateUser() {
      axios.post('http://127.0.0.1:8000/api/users/',{
        username: this.username,
        password: this.password,
      })
      .then(res => {
        console.log(res)
      })
      .catch(err => {
        console.error(err); 
      })
      this.$router.push('/');
    }
      
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