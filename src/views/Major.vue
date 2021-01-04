<template>
    <v-container fluid>
        <h2 class="font-weight-bold">Search by major</h2>
        <v-layout>
        <v-data-iterator
            :items="majors"
            item-key="major"
            :items-per-page="8"
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
                                <h5 class="font-weight-medium">{{ item.major }}</h5>
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
                                    <v-list-item-content class="font-weight-medium">Description of major:</v-list-item-content>
                                    <v-list-item-content class="font-weight-light">
                                        {{item.description}}
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
import json from "/Users/tarakappel/major-connect/backend/majors_json.json";

export default {
  name: "Major",
  data: function() {
    return {
      majors: json.majors,
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