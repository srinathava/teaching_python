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
    <h3 class="text-xl font-bold text-purple-800">The Circus Announcer's Challenge!</h3>
    <p class="text-gray-700">Help our circus announcer combine words to create the perfect announcement!</p>
  </div>

  <div class="flex flex-col md:flex-row items-center justify-center gap-2 mb-6">
    <!-- First String -->
    <div class="bg-red-100 p-4 rounded-lg shadow-md text-center">
      <div class="bg-red-200 p-2 rounded-t-lg font-bold text-red-800">First Word</div>
      <div class="bg-white p-4 rounded-b-lg">
        <span class="text-2xl font-bold text-red-800">"Hello"</span>
      </div>
    </div>

    <!-- Plus Sign -->
    <div class="text-3xl font-bold text-purple-800 my-2">+</div>

    <!-- Space String -->
    <div class="bg-yellow-100 p-4 rounded-lg shadow-md text-center">
      <div class="bg-yellow-200 p-2 rounded-t-lg font-bold text-yellow-800">Space</div>
      <div class="bg-white p-4 rounded-b-lg">
        <span class="text-2xl font-bold text-yellow-800">" "</span>
        <div class="text-xs text-yellow-600">(a space)</div>
      </div>
    </div>

    <!-- Plus Sign -->
    <div class="text-3xl font-bold text-purple-800 my-2">+</div>

    <!-- Second String -->
    <div class="bg-blue-100 p-4 rounded-lg shadow-md text-center">
      <div class="bg-blue-200 p-2 rounded-t-lg font-bold text-blue-800">Second Word</div>
      <div class="bg-white p-4 rounded-b-lg">
        <span class="text-2xl font-bold text-blue-800">"World"</span>
      </div>
    </div>

    <!-- Equals Sign -->
    <div class="text-3xl font-bold text-purple-800 my-2">=</div>

    <!-- Result Box -->
    <div class="bg-green-100 p-4 rounded-lg shadow-md text-center border-2 border-dashed border-green-500">
      <div class="bg-green-200 p-2 rounded-t-lg font-bold text-green-800">Announcement</div>
      <div class="bg-white p-4 rounded-b-lg">
        <span class="text-2xl font-bold text-green-800">"Hello World"</span>
        <div class="text-green-600 mt-1">Store in 'message'</div>
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
      <p>💡 <strong>Hint:</strong> In Python, we can combine text (strings) using the + symbol! Each piece of text needs to be in quotes, like "Hello". If you want a space between words, you need to add it as its own string: " ". Otherwise, the words will be stuck together like "HelloWorld"!</p>
    </div>
  {/if}
</div>