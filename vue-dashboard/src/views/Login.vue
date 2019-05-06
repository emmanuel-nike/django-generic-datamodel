<template>
  <div class="row justify-content-center">
    <div class="col-lg-5 col-md-7">
      <div class="card bg-secondary shadow border-0">
        <div class="card-header bg-transparent">
          <div class="text-muted text-center mt-2 mb-3">
            <h3>Sign In</h3>
            <small>
              Default credentials
              <br>bctest/bctest123
            </small>
          </div>
        </div>
        <div class="card-body px-lg-5 py-lg-4">
          <base-alert v-if="errors.message" type="danger">{{ errors.message }}</base-alert>
          <form role="form" @submit.prevent="login">
            <base-input
              class="input-group-alternative mb-3"
              placeholder="Username"
              addon-left-icon="ni ni-circle-08"
              v-model="model.username"
            ></base-input>

            <base-input
              class="input-group-alternative"
              placeholder="Password"
              type="password"
              addon-left-icon="ni ni-lock-circle-open"
              v-model="model.password"
            ></base-input>

            <div class="text-center">
              <base-button type="primary" @click="login" class="my-4">Sign in</base-button>
            </div>
          </form>
        </div>
      </div>
      <div class="row mt-3">
        <div class="col-6">
          <a href="#" class="text-light">
            <small>Forgot password?</small>
          </a>
        </div>
        <div class="col-6 text-right">
          <router-link to="/register" class="text-light">
            <small>Create new account</small>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "login",
  data() {
    return {
      errors: {
        message: null
      },
      model: {
        username: "",
        password: ""
      }
    };
  },
  methods: {
    login: function() {
      let username = this.model.username;
      let password = this.model.password;
      this.$store
        .dispatch("login", { username, password })
        .then(() => this.$router.push("/"))
        .catch(err => {
          if (
            err.response.status == 400 ||
            err.response.status == 422 ||
            err.response.status == 401
          )
            this.errors.message = "Invalid login credentials";
        });
    }
  },
  watch: {
    model: {
      handler: function(val, oldVal) {
        this.errors.message = null;
      },
      deep: true
    }
  }
};
</script>
<style>
</style>
