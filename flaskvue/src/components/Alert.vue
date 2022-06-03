<template>
  <div>
    <b-alert variant="success" show dismissible>
      <strong style="color:#535c68">{{message}}</strong>
    </b-alert>
    <br>
  </div>
</template>

<script>
  export default{
    props:['message']
  }
</script>

<style>

</style>
