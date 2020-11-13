<template>
  <d-container fluid class="main-content-container px-4">
    <!-- Page Header -->
    <div class="page-header row no-gutters py-4">
      <div class="col-12 col-sm-4 text-center text-sm-left mb-0">
        <h3 class="dashboardHeader page-title">Contributor Data</h3>
      </div>
    </div>

    <d-row>

      <d-col v-for="index in 8" :key="index" lg="6" md="6" sm="12" class="mb-4">

        <d-card class="card-small card-post card-post--1">

          <div style="min-height: 34.2px !important;" v-if="loading">
            <spinner class="dashboardSpinner"></spinner>
          </div>

          <d-card-body v-if="!loading">

            <div v-if="index === 1" id="average_commits_per_PR">

            </div>
            <div v-if="index === 2" id="average_comments_per_PR">

            </div>
            <div v-if="index === 3" id="PR_counts_by_merged_status">

            </div>
            <div v-if="index === 4" id="mean_response_times_for_PR">

            </div>
             <div v-if="index === 5" id="mean_days_between_PR_comments">

            </div>
            <div v-if="index === 6" id="PR_time_to_first_response">

            </div>
            <div v-if="index === 7" id="average_PR_events_for_closed_PRs">

            </div>
            <div v-if="index === 8" id="Average_PR_duration">

            </div>

          </d-card-body>

        </d-card>

      </d-col>

    </d-row>

  </d-container>
</template>

<script lang="ts">
import { mapActions, mapGetters, mapMutations } from "vuex";
import Component from "vue-class-component";
import Vue from "vue";
import axios from "axios";
import * as Bokehjs from 'bokehjs';
import InsightChart from "../components/charts/InsightChart.vue";
import Spinner from "../components/Spinner.vue";
@Component({
  methods: {
    ...mapActions("common", []),
  },
  computed: {
    ...mapGetters("common", ["baseURL"]),
  },
  components: {
    InsightChart,
    Spinner,
  },
})
export default class InsightsPage extends Vue {
  // Data properties
  colors: any = ["#FFC107", "#FF3647", "#159dfb", "#343a40"];
  themes: any = ["warning", "danger", "royal-blue", "dark"];
  api_calls: string[] = ["average_commits_per_PR", "average_comments_per_PR", "PR_counts_by_merged_status", "mean_response_times_for_PR", "mean_days_between_PR_comments", "average_PR_events_for_closed_PRs", "Average_PR_duration"]
  paramaters: any = {repo_id: 25158, start_date: "2019-01-01", end_date: "2020-03-30", return_json: true,}
  responses: any = [];
  loading: boolean = true;
  errored: boolean = false;
  baseURL!: any;
  color_mapping: any = {};
  pageData: any = [];
 mounted() {
    console.log(this.baseURL);

    let api_end: string;

    for(api_end of this.api_calls){

      if(api_end != "returning_contributors_pie_chart"){
       
        (this.paramaters).remove_outliers = 5;
      }

      axios.get(`http://localhost:5000/api/unstable/pull_request_reports/${api_end}/`,{params: this.paramaters,})
        .then((response) => {
        console.log("Pull Request Page Data: ", response);

        (this.responses).push(response.data);

        if(api_end === "Average_PR_duration"){
          this.loading = false
        }

        return Bokehjs.embed.embed_item(response.data);
      }).catch(error => {
        console.log("Pull Request Page Error: ", error);
        this.errored = true
        this.loading = false
      }).finally(() => this.loading = false)

    }
  }
  //Functions go here

}
</script>

<style scoped>

#Average_PR_duration{
  border: black 1px solid;
}

</style>
