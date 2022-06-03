<template>
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
</template>

<script>

</script>

<style>

</style>
