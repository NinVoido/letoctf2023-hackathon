<template>
  <div class="get_user ">
    <h1>Пользователи</h1>
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
  name: 'get_user',
  data()
  {
    return{
      columns: [ 'id', 'name', 'admin', 'team'],
      items:[],
      hostname: this.$api,
        date: this.$date

    }
  },
  async mounted()
  {
    axios.get(`${this.hostname}/user`)
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
