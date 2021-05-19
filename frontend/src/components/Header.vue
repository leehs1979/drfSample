<template>
    <div class="">
        <b-navbar toggleable="lg" type="dark" variant="info">
            <b-navbar-brand class="text-white" href="#">Youtube Rater</b-navbar-brand>
            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

            <b-navbar-nav class="ml-auto">
                <b-nav-form @submit.prevent="login" v-if="token==null">
                    <b-form-input id="username" size="sm" class="mr-sm-2" v-model="username" placeholder="username" name="username"></b-form-input>
                    <b-form-input id="password" size="sm" class="mr-sm-2" v-model="password" placeholder="password" name="password"></b-form-input>
                    
                    <b-button size="sm" class="my-2 my-sm-0" type="submit">Login</b-button>
                </b-nav-form>

                <b-nav-form @submit.prevent="logout" v-if="token!=null">
                                       
                    <b-button size="sm" class="my-2 ml-2" type="submit">Logout</b-button>
                </b-nav-form>

                <b-nav-form @submit.prevent="register" v-if="token === ''">                                       
                    <b-button :to="{name: 'register'}" size="sm" class="my-2 ml-2" type="submit">Register</b-button>
                </b-nav-form>

            </b-navbar-nav>
        </b-navbar>
    </div>
</template>

<script>
import axios from 'axios'
import { TokenService } from '../storage/service'

export default {
    name: 'Header',
    components: {

    },
    data() {
        return {
            username: '',
            password: '',
            token: localStorage.getItem('user-token') || null,
        }
    },
    methods: {
        login() {
            axios.post('http://127.0.0.1:8000/auth/',{
                username: this.username,
                password: this.password,
            })
            .then(res => {
                //console.log(res.data.token)
                this.token = res.data.token
                console.log(this.token)
                localStorage.setItem('user-token', res.data.token)
            })
            .catch(err => {
                //console.error(err); 
                localStorage.removeItem('user-token');
               
            })
        },
        logout() {
            localStorage.removeItem('user-token');
            this.token = null;
        },
        register() {
            console.log('Router')
        },

    },
    created() {
        this.token = TokenService.getToken() || null;
    },
}
</script>