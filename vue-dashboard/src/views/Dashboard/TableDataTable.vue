<template>
  <div class="card">
    <div class="card-header border-0">
      <div class="row align-items-center">
        <div class="col">
          <h3 class="mb-0">{{ compTableName }}</h3>
        </div>
        <div class="col text-right">
          <a
            href="#!"
            v-show="tableColumns.length > 0"
            @click="toggleAddDataModal"
            class="btn btn-sm btn-primary"
          >Add Table Data</a>
        </div>
      </div>
    </div>

    <div class="table-responsive">
      <base-table thead-classes="thead-light" :data="table_data">
        <template slot="columns">
          <th v-for="opt in tableColumns" :key="opt.id">{{ opt.name }}</th>
          <th v-if="tableColumns.length">Action</th>
        </template>

        <template slot-scope="{row}">
          <td v-for="data in row.row_contents" :key="data.id">{{data.content}}</td>
          <td>
            <base-button
              size="sm"
              type="danger"
              iconOnly
              icon="fa fa-trash"
              @click="deleteRow(row.id)"
              title="Delete"
            ></base-button>
          </td>
        </template>
        <tr v-if="table_data.length == 0" slot="custom-row">
          <td :colspan="tableColumns.length">
            <center>Table has no data</center>
          </td>
        </tr>
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

    <modal :show="showAddDataModal" @close="toggleAddDataModal">
      <div slot="header">Add/Edit Data</div>
      <div>
        <base-alert v-if="errors.message" type="danger">{{ errors.message }}</base-alert>
        <form role="form">
          <div v-for="field in tableColumns" :key="field.id">
            <base-input
              v-if="field.field_type != 3"
              class="input-group-alternative mb-3"
              :placeholder="field.name"
              :type="getFieldType(field.field_type)"
              v-model="tableModel[field.id]"
            ></base-input>
            <base-select
              v-else
              class="input-group-alternative mb-3"
              v-model="tableModel[field.id]"
              :options="getSelectOptions(field.field_options)"
            ></base-select>
          </div>
        </form>
      </div>
      <div slot="footer">
        <base-button type="primary" class="sm" @click="saveData">Save</base-button>
      </div>
    </modal>
  </div>
</template>
<script>
export default {
  name: "table-data-table",
  props: {
    tableName: {
      type: String,
      default: "No table selected",
      description: "Selected table name"
    },
    tableId: {
      type: Number,
      description: "Selected table ID"
    },
    tableColumns: {
      type: Array,
      description: "Table columns from fields"
    }
  },
  updated() {
    this.loadTableData();
  },
  data() {
    return {
      errors: {
        message: null
      },
      showAddDataModal: false,
      tableModel: {},
      table_data: [],
      showDialogModal: false,
      dialogMessage: null
    };
  },
  methods: {
    loadTableData: function() {
      let dt = this;
      this.$http.get("/api/data-table/" + this.tableId + "/rows").then(resp => {
        dt.table_data = resp.data;
        for (let i in dt.table_data) {
          if (dt.tableColumns.length > dt.table_data[i].row_contents.length) {
            let row_data = [];
            for (let j in dt.tableColumns) {
              let foundobj = dt.hasField(
                dt.tableColumns[j],
                dt.table_data[i].row_contents
              );

              if (foundobj) {
                row_data.push(foundobj);
              } else {
                row_data.push({
                  content: null,
                  field_id: dt.tableColumns[j].field_id,
                  id: 0,
                  row_id: dt.table_data[i].id,
                  table_id: dt.tableColumns[j].table_id,
                  user_id: dt.tableColumns[j].user_id
                });
              }
            }
            dt.table_data[i].row_contents = row_data;
          }
        }
      });
    },
    hasField: function(obj, objArray) {
      for (let i in objArray) {
        if (objArray[i].field_id == obj.id) return objArray[i];
      }
      return false;
    },
    toggleAddDataModal: function(toggle = !this.showAddDataModal) {
      this.showAddDataModal = toggle;
    },
    toggleDialogModal: function(toggle = !this.showDialogModal) {
      this.showDialogModal = toggle;
    },
    showDialog: function(message, yesFunction) {
      this.dialogMessage = message;
      this.dialogYes = function() {
        yesFunction();
        this.toggleDialogModal();
      };
      this.toggleDialogModal();
    },
    dialogYes: function() {},
    dialogNo: function() {
      this.toggleDialogModal();
    },
    getSelectOptions: function(options) {
      if (options) {
        options = options.split(",");
        return options.map(function(currentValue) {
          currentValue = currentValue.trim();
          return { value: currentValue, name: currentValue };
        });
      }
      return [];
    },
    getFieldType: function(type) {
      if (type == 1) {
        return "number";
      } else if (type == 2) {
        return "date";
      } else {
        return "text";
      }
    },
    saveData: function() {
      console.log(this.tableModel, this.tableData);
      let data = [];
      for (let i in this.tableModel) {
        data.push({
          content: this.tableModel[i],
          field_id: i
        });
      }
      let dt = this;
      this.$http
        .post("/api/data-table/" + this.tableId + "/rows", data)
        .then(() => {
          dt.tableModel = {};
          dt.$notify({ type: "success", title: "Data added successfully" });
          dt.loadTableData();
        })
        .catch(err => {
          console.log(err);
        });
    },
    deleteRow: function(id) {
      let dt = this;
      this.showDialog("Are you sure you want to delete this row data?", () => {
        dt.$http
          .delete("/api/data-table/" + this.tableId + "/row/" + id)
          .then(() => {
            dt.loadTableData();
            dt.$notify({
              type: "success",
              title: "Row data deleted successfully"
            });
          });
      });
    }
  },
  computed: {
    compTableName: function() {
      return this.tableName == null ? "No table selected" : this.tableName;
    }
  }
};
</script>
<style>
</style>
