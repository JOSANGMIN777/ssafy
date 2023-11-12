
<script setup>
    import MainPage from '@/components/MainPage.vue'
    import {ref} from 'vue'
    import {RouterLink, RouterView} from 'vue-router'

</script>

<template>
    <div>
        <MainPage />
    </div>
    <div>
        <nav>
            <RouterLink :to="{name: 'some'}">some</RouterLink> |
            <RouterLink :to="{name: 'other'}">other</RouterLink>    
        </nav>
    </div>
    <RouterView />
</template>

<style scoped>

</style>