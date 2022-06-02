<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1 class="h1">Books</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm">Add Book</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Author</th>
              <th scope="col">Read?</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(book,index) in books" :key="index">
              <td>{{book.title_book}}</td>
              <td>{{book.author_book}}</td>
              <td>
                <span v-if="book.is_reading_book">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <div class="btn-group" role="button">
                  <button class="btn btn-warning btn-sm">Update</button>
                  <button class="btn btn-danger btn-sm">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  export default{
    data(){
      return{
        books:[]
      }
    },
    methods:{
      getBooks(){
        axios.get('http://127.0.0.1:5000/books')
          .then((response)=>{
            this.books = response.data.books
          })
          .catch((err)=>{
            console.log('Error List Books')
            console.log(err)
          })
      },
    },
    created(){//each render page render created hook()
      this.getBooks()
    }
  }
</script>

<style>

</style>
