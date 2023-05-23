<template>
  <div>
    
    <div v-for="(errors, field) in authError" :key="field">
        <div>
            <div v-for="(error, idx) in errors" :key="idx">
                <div id="debug" v-if="error" class="text-center mb-3">ID 또는 PW를 정확히 입력 해 주십시오.</div>
                <div v-else></div>
            </div>
        </div>
    </div>

  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
    name: 'AccountErrorList',
    computed: {
        ...mapGetters(['authError'])
    },
    mounted() {
        setTimeout(() => { location.reload(), 2000})
    }
}
</script>

<style>

</style>