<template>
    <v-container fluid>
        <h2 class="font-weight-medium" align="center">By interest</h2>
        <h3 class="font-weight-light" align="center">Select any that appeal to you - you can always remove them later!</h3>
        <v-chip-group
            multiple
            active-class="primary--text"
        >
            <v-chip
                v-for="job in job_titles"
                :key="job"
            >
            {{ job }}
            </v-chip>
        </v-chip-group>
    </v-container>
</template>

<script>
//import data from "/Users/tarakappel/major-connect/backend/app.py";

export default {
  name: "Major",
  data: function() {
    return {
      job_titles: //data.job_title, // passing array data into Vue
        ['Product Manager', 'Engineer'],
    };
  },

  mounted: function() {
    // Checking if everything works, delete this right after you see that everything works
    console.log(this.job_titles);
  },
};
</script>

<style scoped>
</style>