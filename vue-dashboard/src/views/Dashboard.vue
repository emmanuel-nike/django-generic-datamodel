<template>
  <div>
    <base-header type="gradient-success" class="pb-6 pb-8 pt-5 pt-md-8">
      <!-- Card stats -->
      <div class="row">
        <div class="col-md-4">
          <stats-card
            title="Total tables"
            type="gradient-red"
            :sub-title="tableCount"
            icon="ni ni-calendar-grid-58"
            class="mb-4 mb-xl-0"
          ></stats-card>
        </div>
        <div class="col-md-4">
          <stats-card
            title="Total fields"
            type="gradient-orange"
            :sub-title="fieldCount"
            icon="ni ni-chart-pie-35"
            class="mb-4 mb-xl-0"
          ></stats-card>
        </div>
        <div class="col-md-4">
          <stats-card
            title="Total Data"
            type="gradient-green"
            :sub-title="dataCount"
            icon="ni ni-money-coins"
            class="mb-4 mb-xl-0"
          ></stats-card>
        </div>
      </div>
    </base-header>

    <!--Charts-->
    <div class="container-fluid mt--7">
      <!--Tables-->
      <div class="row mt-5">
        <div class="col-xl-4">
          <data-tables-table
            @tableCount="setTableCount"
            @fieldCount="setFieldCount"
            @selectedTable="setSelectedTable"
          ></data-tables-table>
        </div>
        <div class="col-xl-8 mb-5 mb-xl-0">
          <table-data-table
            :tableName="tableData.name"
            :tableColumns="tableData.columns"
            :tableId="tableData.id"
            @dataUpdated="getDataCount"
          ></table-data-table>
        </div>
      </div>
      <!--End tables-->
    </div>
  </div>
</template>
<script>
// Tables
import DataTablesTable from "./Dashboard/DataTablesTable";
import TableDataTable from "./Dashboard/TableDataTable";

export default {
  components: {
    TableDataTable,
    DataTablesTable
  },
  data() {
    return {
      tableCount: 0,
      fieldCount: 0,
      dataCount: 0,
      tableData: {
        id: 0,
        name: null,
        columns: []
      }
    };
  },
  methods: {
    setTableCount: function(value) {
      this.tableCount = value;
    },
    setFieldCount: function(value) {
      this.fieldCount = value;
    },
    setSelectedTable: function(value) {
      this.tableData.columns = value.fields;
      this.tableData.name = value.name;
      this.tableData.id = value.id;
    },
    getDataCount: function() {
      this.$http
        .get("/api/data-rows/count")
        .then(resp => (this.dataCount = resp.data));
    }
  },
  mounted() {
    this.getDataCount();
  }
};
</script>
<style></style>
