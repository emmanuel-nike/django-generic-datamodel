<template>
  <div>
    <base-header
      class="header pb-8 pt-5 pt-lg-8 d-flex align-items-center"
      style="min-height: 600px; background-image: url(/static/img/theme/profile-cover.jpg); background-size: cover; background-position: center top;"
    >
      <!-- Mask -->
      <span class="mask bg-gradient-success opacity-8"></span>
      <!-- Header container -->
      <div class="container-fluid d-flex align-items-center">
        <div class="row">
          <div class="col-md-11">
            <h1 class="display-2 text-white">{{ userFullName }}</h1>
            <p
              class="text-white mt-0 mb-5"
            >This is your profile page. You can edit your profile information</p>
          </div>
        </div>
      </div>
    </base-header>

    <div class="container-fluid mt--7">
      <div class="row">
        <div class="col-xl-4 order-xl-2 mb-5 mb-xl-0">
          <div class="card card-profile shadow">
            <div class="row justify-content-center">
              <div class="col-lg-3 order-lg-2">
                <div class="card-profile-image">
                  <a href="#">
                    <img src="/static/img/theme/team-4-800x800.jpg" class="rounded-circle">
                  </a>
                </div>
              </div>
            </div>
            <div class="card-header text-center border-0 pt-8 pt-md-4 pb-2 pb-md-4"></div>
            <div class="card-body pt-1 mt-2 pt-md-4">
              <div class="text-center mt-md-5">
                <h3>{{ userFullName }}</h3>
                <div class="h5 font-weight-300">
                  <i class="ni location_pin mr-2"></i>
                  {{ model.username }}
                </div>
                <div class="h5 mt-4">
                  <i class="ni business_briefcase-24 mr-2"></i>
                  {{ model.email }}
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="col-xl-8 order-xl-1">
          <card shadow type="secondary">
            <div slot="header" class="bg-white border-0">
              <div class="row align-items-center">
                <div class="col-8">
                  <h3 class="mb-0">My account</h3>
                </div>
                <div class="col-4 text-right">
                  <a href="#!" class="btn btn-sm btn-primary">Save</a>
                </div>
              </div>
            </div>
            <template>
              <form @submit.prevent>
                <h6 class="heading-small text-muted mb-4">User information</h6>
                <div class="pl-lg-4">
                  <div class="row">
                    <div class="col-lg-6">
                      <base-input
                        alternative
                        label="Username"
                        placeholder="Username"
                        input-classes="form-control-alternative"
                        v-model="model.username"
                      />
                    </div>
                    <div class="col-lg-6">
                      <base-input
                        alternative
                        label="Email address"
                        placeholder="jesse@example.com"
                        input-classes="form-control-alternative"
                        v-model="model.email"
                      />
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-lg-6">
                      <base-input
                        alternative
                        label="First name"
                        placeholder="First name"
                        input-classes="form-control-alternative"
                        v-model="model.first_name"
                      />
                    </div>
                    <div class="col-lg-6">
                      <base-input
                        alternative
                        label="Last name"
                        placeholder="Last name"
                        input-classes="form-control-alternative"
                        v-model="model.last_name"
                      />
                    </div>
                  </div>
                </div>
              </form>
            </template>
          </card>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "user-profile",
  data() {
    return {
      model: {
        username: "",
        email: "",
        first_name: "",
        last_name: "",
        about: ""
      }
    };
  },
  mounted() {
    console.log(this.$store.state.user);
    if (
      typeof this.$store.state.user != "undefined" &&
      typeof this.$store.state.user.first_name != "undefined"
    ) {
      this.setModel(this.$store.state.user);
    } else {
      this.$store
        .dispatch("getUser")
        .then(resp => this.setModel(resp.data))
        .catch(err => {
          console.log(err);
          this.$router.push("login");
        });
    }
  },
  methods: {
    setModel(user) {
      this.model.username = user.username;
      this.model.email = user.email;
      this.model.first_name = user.first_name;
      this.model.last_name = user.last_name;
    }
  },
  computed: {
    userFullName() {
      return typeof this.$store.state.user == "undefined" ||
        typeof this.$store.state.user.first_name == "undefined"
        ? ""
        : this.$store.state.user.first_name +
            " " +
            this.$store.state.user.last_name;
    }
  }
};
</script>
<style></style>
