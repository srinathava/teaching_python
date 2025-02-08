<script lang="ts">
  import { base } from "$app/paths";
  import type { Exercise } from '$lib/server/content/types';
  export let exercise: Exercise;
</script>

<div class="flex justify-center items-center p-4">
  <img 
    src="{base}/images/fruits.webp" 
    alt="Alex and Sam need to swap their fruits" 
    class="max-w-full h-auto rounded-lg shadow-lg"
    width="400px"
  />
</div>