<template>
    <div class="scoreboard_team ">
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
    name: 'scoreboard_team',
    data()
    {
      return{
        columns: [ 'score', 'id', 'name', 'team'],
        items:[],
        hostname: this.$api

      }
    },
    async mounted()
    {
      let result = axios.get(`${this.hostname}/score/user`);
      console.warn((await result).data.data.content)
      this.items = (await result).data.data.content
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
  