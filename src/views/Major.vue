<template>
    <v-container fluid>
        <v-layout>
            <h1>Major page</h1>
        <v-chip-group
            multiple
            active-class="primary--text"
        >
            <v-chip @click="alarm"
                v-for="job_data in job_titles"
                :key="job_data.job_title"
            >
            {{ job_data.job_title }}
            </v-chip>
        </v-chip-group>
        </v-layout>
    </v-container> 
</template>

<script>
import json from "/Users/tarakappel/major-connect/backend/app2.json";

export default {
  name: "Major",
  data: function() {
    return {
      job_titles: json.job_titles,
    };
  },

  mounted: function() {
    // Checking if everything works, delete this right after you see that everything works
    console.log(this.job_titles);
  },

  methods: {
      alarm() {
          alert('Job title alert')
      },
  }
};
</script>

<style scoped>
</style>