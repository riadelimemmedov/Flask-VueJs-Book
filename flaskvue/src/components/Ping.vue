<template>
  <div class="container">
      <button type="submit" class="btn btn-primary">{{msg}}</button>
  </div>
</template>

<script>
  import axios from 'axios'
  export default{
    data(){
      return{
        msg:''
      }
    },
    methods:{
      getMessage(){
        const path = 'http://127.0.0.1:5000/ping'
        axios.get(path)
          .then((response)=>{
            console.log('Successfully Send MESSAGE')
            console.log(response)
            this.msg = response.data
          })
          .catch((err)=>{
            console.log('Erros Send Message')
            console.log(err)
          })
      }
    },
    created(){
      //each page render call this.getmessage function
      this.getMessage()
    }
  }
</script>

<style>

</style>
