<template>
    <div>
    <v-toolbar app color="#8C9EFF" dense>
        <router-link to='/'>
            <v-icon medium>
                mdi-home
            </v-icon>
        </router-link>
       
        <v-row align="center" justify="space-around">
             <v-toolbar-title>Browse by...</v-toolbar-title>
            <v-btn flat>
                <router-link to='/interest'>
                Interest
                </router-link>
            </v-btn>
            <v-btn flat>
                <router-link to='/salary'>
                Salary
                </router-link>
            </v-btn>
            <v-btn flat>
                <router-link to='/career'>
                Career
                </router-link>
            </v-btn>
            <v-btn flat>
                <router-link to='/major'>
                Major
                </router-link>
            </v-btn>
            <v-btn flat>
                <router-link to='/skill'>
                Skill
                </router-link>
            </v-btn>
        </v-row>
    </v-toolbar>
    </div>
</template>

<script>
export default {
    name: 'AppNavigation',
    data () {
        return {
            appTitle: 'MajorConnect',
            items: [
                { title: 'Interest' },
                { title: 'Major' },
                { title: 'Salary' },
                { title: 'Career' },
                { title: 'Skill' },
            ]
        };
    }
};
</script>

<style scoped>
    a {
        color: white;
        text-decoration: none;
    }
</style>