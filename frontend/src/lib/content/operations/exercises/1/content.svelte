<script lang="ts">
  import { fade } from 'svelte/transition';
  import type { Exercise } from '$lib/server/content/types';
  export let exercise: Exercise;
  
  let showHint = false;
  
  function toggleHint() {
    showHint = !showHint;
  }
</script>

<div class="mb-6">
  <div class="text-center mb-4">
    <h3 class="text-xl font-bold text-purple-800">Welcome to the Number Juggler's Show!</h3>
    <p class="text-gray-700">Help our circus juggler add these numbers together!</p>
  </div>

  <div class="flex flex-col md:flex-row items-center justify-center gap-4 mb-6">
    <!-- First Number -->
    <div class="bg-red-100 p-4 rounded-lg shadow-md text-center w-40">
      <div class="bg-red-200 p-2 rounded-t-lg font-bold text-red-800">Juggling Ball #1</div>
      <div class="bg-white p-6 rounded-b-lg">
        <span class="text-4xl font-bold text-red-800">5</span>
      </div>
    </div>

    <!-- Plus Sign -->
    <div class="text-5xl font-bold text-purple-800 my-2">+</div>

    <!-- Second Number -->
    <div class="bg-blue-100 p-4 rounded-lg shadow-md text-center w-40">
      <div class="bg-blue-200 p-2 rounded-t-lg font-bold text-blue-800">Juggling Ball #2</div>
      <div class="bg-white p-6 rounded-b-lg">
        <span class="text-4xl font-bold text-blue-800">3</span>
      </div>
    </div>

    <!-- Equals Sign -->
    <div class="text-5xl font-bold text-purple-800 my-2">=</div>

    <!-- Result Box -->
    <div class="bg-purple-100 p-4 rounded-lg shadow-md text-center w-40 border-2 border-dashed border-purple-500">
      <div class="bg-purple-200 p-2 rounded-t-lg font-bold text-purple-800">Total Juggling Balls</div>
      <div class="bg-white p-6 rounded-b-lg">
        <span class="text-4xl font-bold text-purple-800">?</span>
        <div class="text-purple-600 mt-2">Store in 'sum'</div>
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
      <p>💡 <strong>Hint:</strong> In Python, we use the + symbol to add numbers together! When we write sum = 5 + 3, we're telling Python to add 5 and 3, then store the result in a variable called 'sum'.</p>
    </div>
  {/if}
</div>