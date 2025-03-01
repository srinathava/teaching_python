<script lang="ts">
  import { base } from "$app/paths";
  import { fade } from 'svelte/transition';
  import type { Exercise } from '$lib/server/content/types';
  export let exercise: Exercise;
  
  let showHint = false;
  
  function toggleHint() {
    showHint = !showHint;
  }
</script>

<div>
  <div class="flex justify-center items-center p-4">
    <img
      src="{base}/images/fruits.webp"
      alt="Alex and Sam need to swap their fruits"
      class="max-w-full h-auto rounded-lg shadow-lg"
      width="400px"
    />
  </div>
  
  <!-- Hint section at the bottom of content -->
  <div class="flex justify-end mb-2">
    <button
      class="text-yellow-600 hover:text-yellow-800 flex items-center text-sm"
      on:click={toggleHint}
    >
      <span class="mr-1">💡</span>
      <span>{showHint ? 'Hide hint' : 'Need a hint?'}</span>
    </button>
  </div>
  
  {#if showHint}
    <div class="mb-4 p-3 bg-yellow-50 text-yellow-800 rounded-lg border border-yellow-200" transition:fade>
      <p>💡 <strong>Hint:</strong> Think about how you can temporarily store one fruit while you make the swap!</p>
    </div>
  {/if}
</div>