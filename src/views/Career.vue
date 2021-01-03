<template>
    <v-container fluid>
        <h2 class="font-weight-bold">Search by career</h2>
        <v-layout>
        <v-data-iterator
            :items="job_titles"
            item-key="job_title"
            :items-per-page="4"
            :single-expand="singleExpand"
        >
            <template v-slot:default="{ items, isExpanded, expand}">
                <v-row>
                    <v-col
                        v-for="item in items"
                        :key="item.job_title"
                        cols="8"
                    >
                        <v-card
                            class="mx-auto"
                        >
                            <v-card-title>
                                <h5 class="font-weight-medium">{{ item.job_title }}</h5>
                            </v-card-title>
                            <v-switch
                                :input-value="isExpanded(item)"
                                :label="isExpanded(item) ? 'Collapse' : 'Learn more'"
                                class="pl-4 mt-0"
                                @change="(v) => expand(item,v)"
                            >
                            </v-switch>
                            <v-divider></v-divider>
                            <v-list 
                                flat
                                v-if="isExpanded(item)"
                            >
                                <v-list-item>
                                    <v-list-item-content class="font-weight-medium">Median base salary:</v-list-item-content>
                                    <v-list-item-content class="font-weight-light">
                                        {{item.salary}}
                                    </v-list-item-content>
                                </v-list-item>
                                <v-list-item>
                                    <v-list-item-content class="font-weight-medium">Job description:</v-list-item-content>
                                    <v-list-item-content class="font-weight-light">
                                        {{item.job_description}}
                                    </v-list-item-content>
                                </v-list-item>
                            </v-list>
                            <v-card-actions @click="alarm">
                                <v-btn icon>
                                    <v-icon>mdi-bookmark</v-icon>
                                </v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-col>
                </v-row>
            </template>
        </v-data-iterator>
        </v-layout>
    </v-container> 
</template>

<script>
import json from "/Users/tarakappel/major-connect/backend/app2.json";

export default {
  name: "Career",
  data: function() {
    return {
      job_titles: json.job_titles,
      singleExpand: false,
    };
  },
  methods: {
      alarm() {
          alert('Saving career')
      },
  }
};
</script>

<style scoped>
</style>