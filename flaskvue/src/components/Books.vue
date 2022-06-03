<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1 class="h1">Books</h1>
        <hr><br><br>
        <app-alert :message="message" v-if="showMessage"></app-alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.book-modal>Add Book</button>
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
                  <button
                      type="button"
                      class="btn btn-warning btn-sm"
                      v-b-modal.book-update-modal
                      @click="editBook(book)"
                    >
                    Update
                  </button>
                  <button class="btn btn-danger btn-sm">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <!-- !AddBookVue Modal -->
      <b-modal
    ref="addBookModal"
    id="book-modal"
    title="Add a new book"
    hide-footer
  >
    <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group
        id="form-title-group"
        label="Title:"
        label-for="form-title-input"
      >
        <b-form-input
          id="form-title-input"
          type="text"
          v-model="addBookForm.title"
          required
          placeholder="Enter title"
        >
        </b-form-input>
      </b-form-group>
      <b-form-group
        id="form-author-group"
        label="Author:"
        label-for="form-author-input"
      >
        <b-form-input
          id="form-author-input"
          type="text"
          v-model="addBookForm.author"
          required
          placeholder="Enter author"
        >
        </b-form-input>
      </b-form-group>
      <b-form-group id="form-read-group">
        <b-form-checkbox-group v-model="addBookForm.read" id="form-checks">
          <b-form-checkbox value="true">Read?</b-form-checkbox>
        </b-form-checkbox-group>
      </b-form-group>
      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
      </b-modal>
    <!-- Finish AddBookVue Modal-->

    <!-- !Update Book Modal -->
    <b-modal ref="editBookModal"
          id="book-update-modal"
          title="Update"
          hide-footer>
    <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
    <b-form-group id="form-title-edit-group"
                label="Title:"
                label-for="form-title-edit-input">
      <b-form-input id="form-title-edit-input"
                    type="text"
                    v-model="editForm.title"
                    required
                    placeholder="Enter title">
      </b-form-input>
    </b-form-group>
    <b-form-group id="form-author-edit-group"
                  label="Author:"
                  label-for="form-author-edit-input">
        <b-form-input id="form-author-edit-input"
                      type="text"
                      v-model="editForm.author"
                      required
                      placeholder="Enter author">
        </b-form-input>
      </b-form-group>
    <b-form-group id="form-read-edit-group">
      <b-form-checkbox-group v-model="editForm.read" id="form-checks">
        <b-form-checkbox value="true">Read?</b-form-checkbox><!-- if checked checkbox value="true" default -->
      </b-form-checkbox-group>
    </b-form-group>
    <b-button-group>
      <b-button type="submit" variant="primary">Update</b-button>
      <b-button type="reset" variant="danger">Cancel</b-button>
    </b-button-group>
  </b-form>
    </b-modal>

  </div>
</template>

<script>
  import axios from 'axios'
  import AddBook from './AddBook.vue'
  import Alert from './Alert.vue'
  export default{
    data(){
      return{
        books:[],
        addBookForm:{
          title: '',
          author:'',
          read:[]
        },
        editForm:{
          id:'',
          title:'',
          author:'',
          read:[]
        },
        message: '',
        showMessage:false
      }
    },
    methods:{
      //!getBooks
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
      //allBook
      addBook(payload){
        const path = 'http://127.0.0.1:5000/books'
        axios.post(path,payload)
          .then((response)=>{
            this.getBooks()//after POST request call getBooks() function and list updated book list
            this.message = 'Book Added Successfully...'
            this.showMessage = true
          })
          .catch((err)=>{
            console.log('Post request error')
            console.log(err)
            this.getBooks()
          })
      },
      //initForm
      initForm(){
        this.addBookForm.title = ''
        this.addBookForm.author = ''
        this.addBookForm.read = [],
        this.editForm.id = '',
        this.editForm.title = '',
        this.editForm.author = '',
        this.editForm.read = []
      },
      //onSubmit
      onSubmit(e){
        e.preventDefault()
        this.$refs.addBookModal.hide()//close the model
        let read = false
        if(this.addBookForm.read[0]) read=true;//if selected read assing read=true
        const payload = {
          title : this.addBookForm.title,
          author: this.addBookForm.author,
          read:read
        }
        this.addBook(payload)//send data addBook function
        this.initForm()//after request clear input fields
      },
      //onReset
      onReset(e){//cancel button
        e.preventDefault()
        this.$refs.addBookForm.hide()
        this.initForm()
      },
      editBook(book){
        console.log('Is reading book NOT array ', book.is_reading_book)
        console.log('Is reading book YES array ', [book.is_reading_book])

        this.editForm.id = book.id
        this.editForm.title = book.title_book//from vue js template book data
        this.editForm.author = book.author_book
        this.editForm.read = [book.is_reading_book]
        //console.log('Edited Book ', this.editForm)
        //console.log('Edir form read value ', this.editForm.read)
      },
      onSubmitUpdate(e){
        e.preventDefault()
        this.$refs.editBookModal.hide()
        console.log('bunedi ala ', this.editForm.read)
        let read = false;
        if(this.editForm.read.includes('true')){
          alert('True var listede')
          read = true
        }
        //if selected checkbox return readed value true
        console.log('Read value ', read)
        const payload = {
          title:this.editForm.title,
          author:this.editForm.author,
          read:read
        }
        //console.log('buneeee ', this.editForm.read)
        this.updateBook(payload,this.editForm.id)
      },
      updateBook(payload,bookId){
        const path = `http://127.0.0.1:5000/books/${bookId}`
        console.log('update data start => updateBook view')
        axios.put(path,payload)
          .then((response)=>{
            console.log('Successfully update book')
            console.log(response.data)
            this.getBooks()
            this.message = 'Book Updated...'
            this.showMessage = true
          })
          .catch((err)=>{
            console.log('Error updated book')
            console.log(err)
            this.getBooks()
          })
      },
      onResetUpdate(e){//cancel button
        e.preventDefault()
        this.$refs.editBookModal.hide()
        this.initForm()
        this.getBooks()
      }
    },
    components:{
      'app-addbook':AddBook,
      'app-alert':Alert
    },
    created(){//each render page render created hook()
      this.getBooks()
      this.initForm()
    }
  }
</script>

<style>

</style>
