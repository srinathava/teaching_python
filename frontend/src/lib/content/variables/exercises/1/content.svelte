<script lang="ts">
  import { fade } from 'svelte/transition';
  import type { Exercise } from '$lib/server/content/types';
  export let exercise: Exercise;
  
  let showHint = false;
  
  function toggleHint() {
    showHint = !showHint;
  }
</script>

<div>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
    <div class="bg-yellow-100 p-4 rounded-lg shadow-md text-center">
      <div class="bg-yellow-200 p-2 rounded-t-lg font-bold text-yellow-800">Blocks Box</div>
      <div class="bg-white p-4 rounded-b-lg">
        <span class="text-2xl font-bold text-yellow-800">12</span>
        <div class="text-yellow-600">blocks</div>
      </div>
    </div>
    <div class="bg-pink-100 p-4 rounded-lg shadow-md text-center">
      <div class="bg-pink-200 p-2 rounded-t-lg font-bold text-pink-800">Dolls Box</div>
      <div class="bg-white p-4 rounded-b-lg">
        <span class="text-2xl font-bold text-pink-800">5</span>
        <div class="text-pink-600">dolls</div>
      </div>
    </div>
    <div class="bg-blue-100 p-4 rounded-lg shadow-md text-center">
      <div class="bg-blue-200 p-2 rounded-t-lg font-bold text-blue-800">Cars Box</div>
      <div class="bg-white p-4 rounded-b-lg">
        <span class="text-2xl font-bold text-blue-800">8</span>
        <div class="text-blue-600">cars</div>
      </div>
    </div>
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
      <p>💡 <strong>Hint:</strong> Remember to use = to assign values to variables!</p>
    </div>
  {/if}
</div>