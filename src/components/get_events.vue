<template>
    <meta charset="UTF-8"/>
<div id="app">
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
  </div >
</template>

<script>
import axios from "axios"
export default {
  name: 'get_events',
  
  data()
  {
    return{
      columns: [ 'id', 'title', 'speaker', 'start', 'end'],
      items:[],
      hostname: this.$api,
      date: this.$date
    }
  },
  async mounted()
  {
    axios.get(`${this.hostname}/event?date=${this.date}`)
    .then(response => {
          console.warn((response).data.data.content)
          this.items = (response).data.data.content
    })
    .catch(error => {
      if(error){
          this.$router.push('NoEvents')
      }
    });
  
}
}
</script>


<style>
    /* Стили для виджета */
    .widget {
      max-width: 400px auto;
      margin: 20px auto;
      padding: 20px;
      background-color: #f9f9f9;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
      text-align: center;
    }

    .header {
      margin-bottom: 20px;
    }

    .items {
      margin-bottom: 20px;
    }

    .items-table {
      width: 100%;
      position: center;
      border-collapse: collapse;
    }

    .items-table th,
    .items-table td {
      padding: 10px;
      border: 1px solid rgb(169, 182, 233);
    }

    .items-table th {
      background-color: #333; 
      color: #fff;
    }

    .items-table td {
      background-color: #91dbd6;
    }

    .navigation {
      display: flex;
      justify-content: center;
    }

    .navigation button {
      margin: 0 5px;
      padding: 5px 10px;
      border: none;
      background-color: #333;
      color: #fff;
      cursor: pointer;
    }
  </style>