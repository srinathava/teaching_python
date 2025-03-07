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
    <h3 class="text-xl font-bold text-purple-800">The Amazing Circus Height Checker!</h3>
    <p class="text-gray-700">Help the circus check if visitors are tall enough for the thrilling roller coaster!</p>
  </div>

  <div class="flex flex-col md:flex-row items-center justify-center gap-6 mb-6">
    <!-- Visitor -->
    <div class="bg-blue-100 p-4 rounded-lg shadow-md text-center">
      <div class="bg-blue-200 p-2 rounded-t-lg font-bold text-blue-800">Visitor</div>
      <div class="bg-white p-4 rounded-b-lg flex flex-col items-center">
        <div class="text-5xl mb-2">👧</div>
        <div class="text-xl font-bold text-blue-800">145 cm</div>
        <div class="text-sm text-blue-600">visitor_height = 145</div>
      </div>
    </div>

    <!-- Comparison -->
    <div class="flex flex-col items-center">
      <div class="text-3xl font-bold text-purple-800 my-2">≥</div>
      <div class="text-sm text-purple-600">(greater than or equal to)</div>
    </div>

    <!-- Minimum Height -->
    <div class="bg-red-100 p-4 rounded-lg shadow-md text-center">
      <div class="bg-red-200 p-2 rounded-t-lg font-bold text-red-800">Minimum Height</div>
      <div class="bg-white p-4 rounded-b-lg flex flex-col items-center">
        <div class="text-5xl mb-2">📏</div>
        <div class="text-xl font-bold text-red-800">140 cm</div>
        <div class="text-sm text-red-600">min_height = 140</div>
      </div>
    </div>

    <!-- Equals Sign -->
    <div class="text-3xl font-bold text-purple-800 my-2">=</div>

    <!-- Result Box -->
    <div class="bg-green-100 p-4 rounded-lg shadow-md text-center border-2 border-dashed border-green-500">
      <div class="bg-green-200 p-2 rounded-t-lg font-bold text-green-800">Result</div>
      <div class="bg-white p-4 rounded-b-lg flex flex-col items-center">
        <div class="text-2xl font-bold text-green-800">True</div>
        <div class="text-sm text-green-600">is_tall_enough = visitor_height >= min_height</div>
      </div>
    </div>
  </div>

  <div class="bg-purple-100 p-4 rounded-lg shadow-md mb-6">
    <h4 class="font-bold text-purple-800 mb-2">Comparison Operators in Python:</h4>
    <div class="grid grid-cols-2 md:grid-cols-3 gap-3">
      <div class="bg-white p-2 rounded-lg text-center">
        <div class="font-bold text-purple-800">==</div>
        <div class="text-sm text-purple-600">Equal to</div>
      </div>
      <div class="bg-white p-2 rounded-lg text-center">
        <div class="font-bold text-purple-800">!=</div>
        <div class="text-sm text-purple-600">Not equal to</div>
      </div>
      <div class="bg-white p-2 rounded-lg text-center bg-yellow-50">
        <div class="font-bold text-purple-800">>=</div>
        <div class="text-sm text-purple-600">Greater than or equal to</div>
      </div>
      <div class="bg-white p-2 rounded-lg text-center">
        <div class="font-bold text-purple-800">&lt;=</div>
        <div class="text-sm text-purple-600">Less than or equal to</div>
      </div>
      <div class="bg-white p-2 rounded-lg text-center">
        <div class="font-bold text-purple-800">&gt;</div>
        <div class="text-sm text-purple-600">Greater than</div>
      </div>
      <div class="bg-white p-2 rounded-lg text-center">
        <div class="font-bold text-purple-800">&lt;</div>
        <div class="text-sm text-purple-600">Less than</div>
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
      <p>💡 <strong>Hint:</strong> Use the >= (greater than or equal to) operator to compare the visitor's height with the minimum height requirement. This will give you a boolean value (True or False) that you can store in the 'is_tall_enough' variable.</p>
    </div>
  {/if}
</div>