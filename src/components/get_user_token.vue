<template>
    <div class="get_user_token ">
      <h1>Вход</h1>
      <input type="text" name="token" v-model="token" placeholder="Enter Token"/> <br /><br />
      <button v-on:click="signIn"> Sign in</button>
    </div>
  </template>
  
  <script>
  import axios from "axios"
  import VueCookies from 'vue-cookies'
  export default {
    name: 'get_user_token',
    data()
    {
      return{
        token: "",
        hostname: this.$api
        
      }
    },

    methods: {
      config: {
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin":"*",
          "Access-Control-Allow-Methods": "DELETE, POST, GET, OPTIONS",
          "Access-Control-Allow-Headers": "Content-Type, Authorization, X-Requested-With"
          }
        },

        async signIn() {
          axios.get(`${this.hostname}/user/token/${this.token}`, {
            // token:this.token\
            //withCredentials: "include",
          headers: {
           // 'COOKIE': `${VueCookies.$cookies.get("hello")}`,
          }, },)
          .then(response => {
            this.id = (response).data.id
            VueCookies.set("hello", this.id, "1h")
            this.$router.push('StartPage')
          })
          .catch(error => {
            if(error){
              this.$router.push('Login')

            }

          });


        }
    }
    
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  h3 {
    margin: 40px 0 0;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }
  table, th, td {
    border: 1px solid;
    align-self: "center";
  }
  </style>
  