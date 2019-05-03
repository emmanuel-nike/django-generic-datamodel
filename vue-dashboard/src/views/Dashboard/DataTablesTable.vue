<template>
  <div class="card">
    <div class="card-header border-0">
      <div class="row align-items-center">
        <div class="col">
          <h3 class="mb-0">Tables</h3>
        </div>
        <div class="col text-right">
          <base-button size="sm" type="primary" @click="addTable">Add Table</base-button>
        </div>
      </div>
    </div>

    <div class="table-responsive">
      <base-table thead-classes="thead-light" :data="tableData">
        <template slot="columns">
          <th>Name</th>
          <th>Fields</th>
          <th>Action</th>
        </template>

        <template slot-scope="{row}">
          <th scope="row">
            <a href="#" @click="viewTable(row)">{{row.name}}</a>
          </th>
          <td>{{row.fields.length}}</td>
          <td>
            <base-button
              size="sm"
              type="primary"
              iconOnly
              icon="fa fa-eye"
              @click="viewTable(row)"
              title="View"
            ></base-button>
            <base-button
              size="sm"
              type="primary"
              iconOnly
              icon="fas fa-pencil-alt"
              @click="editTable(row)"
              title="Edit"
            ></base-button>
            <base-button
              size="sm"
              type="danger"
              iconOnly
              icon="fa fa-trash"
              @click="deleteTable(row.id)"
              title="Delete"
            ></base-button>
          </td>
        </template>
      </base-table>
    </div>

    <modal :show="showDialogModal" @close="toggleDialogModal">
      <div slot="header">
        <h3>Are You Sure?</h3>
      </div>
      <span>{{ dialogMessage }}</span>
      <div slot="footer">
        <base-button type="default" class="sm" @click="dialogYes">Yes</base-button>
        <base-button type="primary" class="sm" @click="dialogNo">No</base-button>
      </div>
    </modal>

    <modal :show="showModal" @close="toggleTableModal" type="large">
      <div slot="header">Add/Edit Table</div>
      <div>
        <base-alert v-if="errors.message" type="danger">{{ errors.message }}</base-alert>
        <form role="form">
          <base-input
            class="input-group-alternative mb-3"
            placeholder="Table Name"
            :error="errors.tableName"
            @input="errors.tableName = ''"
            v-model="active_table.name"
          ></base-input>
          <base-textarea
            class="input-group-alternative mb-4"
            placeholder="Table Description"
            v-model="active_table.description"
          ></base-textarea>
          <base-table thead-classes="thead-light" :data="active_table.fields">
            <template slot="columns">
              <th>Name</th>
              <th>Type</th>
              <th>Options</th>
              <th>Action</th>
            </template>

            <template slot-scope="{row}">
              <td>
                <base-input class="input-group-sm mb-0" placeholder="Name" v-model="row.name"></base-input>
              </td>
              <td>
                <base-select
                  class="input-group-sm mb-0"
                  v-model="row.field_type"
                  :value="row.field_type"
                  :options="field_types"
                ></base-select>
              </td>
              <td>
                <base-input
                  class="input-group-sm mb-0"
                  v-show="row.field_type == 3"
                  placeholder="Comma separated options"
                  v-model="row.field_options"
                ></base-input>
              </td>
              <td>
                <base-button
                  size="sm"
                  type="danger"
                  iconOnly
                  icon="ni ni-fat-remove"
                  title="Remove"
                  @click="removeField(row.name)"
                ></base-button>
              </td>
            </template>
            <tr slot="custom-row">
              <td>
                <base-input
                  class="input-group-sm mb-0"
                  placeholder="Name"
                  :error="errors.fieldName"
                  @input="errors.fieldName = ''"
                  v-model="new_field.name"
                ></base-input>
              </td>
              <td>
                <base-select
                  class="input-group-sm mb-0"
                  v-model="new_field.field_type"
                  :options="field_types"
                ></base-select>
              </td>
              <td>
                <base-input
                  class="input-group-sm mb-0"
                  v-show="new_field.field_type == 3"
                  placeholder="Comma separated options"
                  :value="new_field.field_options"
                  v-model="new_field.field_options"
                ></base-input>
              </td>
              <td>
                <base-button
                  size="sm"
                  type="primary"
                  iconOnly
                  icon="ni ni-fat-add"
                  title="Add"
                  @click="addField"
                ></base-button>
              </td>
            </tr>
          </base-table>
          <div class="text-center"></div>
        </form>
      </div>
      <div slot="footer">
        <base-button type="primary" class="sm" @click="saveTable">Save</base-button>
      </div>
    </modal>
  </div>
</template>
<script>
export default {
  name: "data-tables-table",
  data() {
    return {
      errors: {
        tableName: null,
        fieldName: null,
        message: null
      },
      tableData: [],
      active_table: {
        fields: []
      },
      new_field: {
        name: null,
        field_type: 0,
        field_options: null
      },
      field_types: [
        { value: 0, name: "Text" },
        { value: 1, name: "Number" },
        { value: 2, name: "Date" },
        { value: 3, name: "enum" }
      ],
      showModal: false,
      showDialogModal: false,
      dialogMessage: null
    };
  },
  mounted() {
    this.loadTables();
  },
  methods: {
    viewTable: function(selectedTable) {
      this.$emit("selectedTable", selectedTable);
    },
    loadTables: function() {
      var dt = this;
      this.$http.get("/api/data-tables").then(response => {
        dt.tableData = [];
        let field_count = 0;
        let table_count = 0;
        for (var d in response.data) {
          dt.tableData.push({
            id: response.data[d].id,
            name: response.data[d].name,
            fields: response.data[d].data_fields
          });
          field_count += response.data[d].data_fields.length;
          table_count += 1;
        }
        dt.$emit("tableCount", table_count);
        dt.$emit("fieldCount", field_count);
      });
    },
    toggleTableModal: function(toggle = !this.showModal) {
      this.showModal = toggle;
    },
    toggleDialogModal: function(toggle = !this.showDialogModal) {
      this.showDialogModal = toggle;
    },
    showDialog: function(message, yesFunction) {
      this.dialogMessage = message;
      let dt = this;
      this.dialogYes = function() {
        yesFunction();
        dt.toggleDialogModal();
      };
      this.toggleDialogModal();
    },
    dialogYes: function() {},
    dialogNo: function() {
      this.toggleDialogModal();
    },
    addTable: function() {
      this.active_table = {
        fields: []
      };
      this.toggleTableModal(true);
    },
    addField: function() {
      if (!this.new_field.name) {
        this.errors.fieldName = "The field name is required";
        return;
      }
      this.new_field.field_type = parseInt(this.new_field.field_type);
      this.active_table.fields.push(this.new_field);
      this.new_field = { name: null, field_type: 0, field_options: null };
    },
    removeField: function(name) {
      let table_id = 0;
      let field_id = 0;
      let pos = -1;
      for (let i = 0; i < this.active_table.fields.length; i++) {
        if (this.active_table.fields[i].name == name) {
          if (this.active_table.id) {
            table_id = this.active_table.id;
            if (this.active_table.fields[i].id) {
              field_id = this.active_table.fields[i].id;
            }
          }
          pos = i;
        }
      }

      //Check if this is an existing field and delete from database
      let dt = this;
      if (table_id && field_id && pos > -1) {
        this.showDialog("Are you sure you want to delete this field?", () => {
          dt.$http
            .delete("/api/data-table/" + table_id + "/field/" + field_id)
            .then(resp => {
              dt.active_table.fields.splice(pos, 1);
            });
        });
      } else if (pos > -1) {
        dt.active_table.fields.splice(pos, 1);
      }
    },
    editTable: function(selectedTable) {
      this.active_table = selectedTable;
      this.toggleTableModal();
    },
    deleteTable: function(id) {
      let dt = this;
      this.showDialog("Are you sure you want to delete this table?", () => {
        dt.$http.delete("/api/data-table/" + id).then(resp => {
          for (let i = 0; i < dt.tableData.length; i++) {
            if (this.tableData[i].id == id) {
              dt.tableData.splice(i, 1);
              break;
            }
          }
        });
      });
    },
    saveTable: function() {
      if (!this.active_table.name) {
        this.errors.tableName = "The table name is required";
        return;
      }
      if (this.active_table.fields.length == 0) {
        this.errors.message = "You must add at least one field";
        return;
      }

      let dt = this;
      if (this.active_table.id) {
        this.$http
          .put("/api/data-table/" + this.active_table.id, {
            name: this.active_table.name,
            description: this.active_table.description
          })
          .then(response => {
            let id = response.data.id;
            for (let i = 0; i < dt.active_table.fields.length; i++) {
              if (dt.active_table.fields[i].id) {
                dt.$http
                  .put(
                    "/api/data-table/" +
                      id +
                      "/field/" +
                      dt.active_table.fields[i].id,
                    {
                      name: dt.active_table.fields[i].name,
                      field_type: dt.active_table.fields[i].field_type,
                      field_options: dt.active_table.fields[i].field_options
                    }
                  )
                  .then(resp => {})
                  .catch(err => {
                    console.log(err);
                  });
              } else {
                dt.$http
                  .post(
                    "/api/data-table/" + id + "/fields",
                    dt.active_table.fields[i]
                  )
                  .then(resp => {})
                  .catch(err => {
                    console.log(err);
                  });
              }
            }
            this.$notify({
              type: "success",
              title: "Table and fields saved successfully"
            });
            dt.resetActiveTableAndCloseModal();
          });
      } else {
        this.$http
          .post("/api/data-tables", {
            name: this.active_table.name,
            description: this.active_table.description
          })
          .then(response => {
            let id = response.data.id;
            for (let i = 0; i < dt.active_table.fields.length; i++) {
              dt.$http
                .post(
                  "/api/data-table/" + id + "/fields",
                  dt.active_table.fields[i]
                )
                .then(resp => {})
                .catch(err => {
                  console.log(err);
                });
            }
            dt.resetActiveTableAndCloseModal();
          });
      }
    },
    resetActiveTableAndCloseModal: function() {
      this.loadTables();
      this.active_table = {
        fields: []
      };
      this.toggleTableModal();
    }
  },
  watch: {
    active_table: {
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
