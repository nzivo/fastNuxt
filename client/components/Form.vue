<template lang="">
  <div>
    <v-form ref="form" v-model="valid" lazy-validation>
      <v-text-field v-if="id" v-model="id"> </v-text-field>
      <v-text-field
        v-model="name"
        :counter="10"
        :rules="nameRules"
        label="Name"
        required
      ></v-text-field>

      <v-text-field
        v-model="email"
        :rules="emailRules"
        label="E-mail Address"
        required
      ></v-text-field>

      <v-text-field
        v-model="password"
        type="password"
        :rules="passwordRules"
        label="Password"
        required
      ></v-text-field>

      <v-btn
        :disabled="!valid"
        color="success"
        class="mr-4"
        @click="submitUser({ id, name, email, password })"
      >
        {{ id ? "Update" : "Submit" }}
      </v-btn>
    </v-form>
  </div>
</template>
<script>
export default {
  data: () => ({
    valid: true,
    nameRules: [
      (v) => !!v || "Name is required",
      (v) => (v && v.length >= 4) || "Name must not be less than 4 characters",
    ],
    emailRules: [
      (v) => !!v || "E-mail is required",
      (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
    ],
    passwordRules: [
      (v) => !!v || "Password is required",
      (v) =>
        (v && v.length >= 8) || "Password should contain least 8 characters",
    ],
  }),

  computed: {
    id: {
      get() {
        return this.$store.state.user.id;
      },
      set(value) {
        this.$store.commit("user/storeId", value);
      },
    },
    name: {
      get() {
        return this.$store.state.user.name;
      },
      set(value) {
        this.$store.commit("user/storeName", value);
      },
    },
    email: {
      get() {
        return this.$store.state.user.email;
      },
      set(value) {
        this.$store.commit("user/storeEmail", value);
      },
    },
    password: {
      get() {
        return this.$store.state.user.password;
      },
      set(value) {
        this.$store.commit("user/storePassword", value);
      },
    },
  },

  methods: {
    async submitUser(user) {
      this.$refs.form.validate();
      if (user.id) {
        await this.$axios.put("http://localhost:8000/users/" + user.id, user);
      } else {
        await this.$axios.post("http://localhost:8000/users", user);
      }
      await this.resetForm({ id: 0, name: "", email: "", password: "" });
      await this.$store.commit(
        "users/storeData",
        await this.$axios.get("http://localhost:8000/users").data
      );
    },
    resetForm(user) {
      this.$store.commit("user/storeId", user.id);
      this.$store.commit("user/storeName", user.name);
      this.$store.commit("user/storeEmail", user.email);
      this.$store.commit("user/storePassword", user.password);
    },
  },
};
</script>
<style lang=""></style>
