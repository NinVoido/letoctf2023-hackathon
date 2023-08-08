<template>
    <div class="challenge_list">
      <h1>challenges</h1>
      <table class="table">
        <thead>
            <tr>
                <th v-for="(column, index) in columns" :key="index"> {{column}}</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(item, index) in items" :key="index">
                <td v-for="(column, indexColumn) in columns" :key="indexColumn">{{item[column]}}</td>
            </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  import axios from "axios"
  export default {
    name: 'challenge_list',
    data()
    {
      return{
        columns: [ 'id', 'name', 'description', 'weight', 'team', 'visible', 'solved', 'start', 'end'],
        items:[],
        hostname: this.$api,
        date: this.$date

      }
    },
    async mounted()
    {
        let userId = 'b0e85bf5-3e44-4845-910e-ceb386376a18';
        axios.get(`http://192.168.14.39:8000/api/v1/challenge?userId=${userId}`)
        .then(response => {
            this.items = (response).data.data.content
        })
        .catch(error => {
        if(error){
            this.$router.push('Login')
        }
        });
    },
    
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
  