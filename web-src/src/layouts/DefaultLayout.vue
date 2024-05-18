<script setup>
import { onMounted } from "vue";
import { themeChange } from "theme-change";

// mounted
onMounted(() => {
  themeChange(false);
});
</script>
<template>
  <div class="h-screen min-h-screen bg-base-200 py-5 font-sans text-base">
    <slot />
  </div>
</template>
