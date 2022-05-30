<template lang="">
  <div>
    <v-data-table
      :headers="headers"
      :items="users"
      :items-per-page="5"
      class="elevation-1"
    >
      <template v-slot:[`item.edit`]="{ item }">
        <v-btn color="primary" @click="editItem(item)">Edit</v-btn>
      </template>
      <template v-slot:[`item.delete`]="{ item }">
        <v-btn color="error" @click="deleteItem(item.id)">Delete</v-btn>
      </template>
    </v-data-table>
  </div>
</template>
<script>
export default {
  data() {
    return {
      headers: [
        { text: "Name", value: "name" },
        { text: "Email Address", value: "email" },
        { text: "Password", value: "password" },
        { text: "Edit", value: "edit" },
        { text: "Delete", value: "delete" },
      ],
    };
  },
  computed: {
    users() {
      return this.$store.state.users.data;
    },
  },
  async fetch() {
    this.$store.commit(
      "users/storeUsers",
      (await this.$axios.get("http://localhost:8000/users/")).data
    );
  },
  methods: {
    editItem(user) {
      this.$store.commit("user/storeId", user.id);
      this.$store.commit("user/storeName", user.name);
      this.$store.commit("user/storeEmail", user.email);
      this.$store.commit("user/storePassword", user.password);
    },
    async deleteItem(id) {
      await this.$axios.delete("http://localhost:8000/users/" + id);
      this.$store.commit(
        "users/storeUsers",
        (await this.$axios.get("http://localhost:8000/users/")).data
      );
    },
  },
};
</script>
<style lang=""></style>
