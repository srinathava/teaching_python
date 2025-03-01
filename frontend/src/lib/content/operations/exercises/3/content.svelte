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
    <h3 class="text-xl font-bold text-purple-800">The Great Circus Animal Feast!</h3>
    <p class="text-gray-700">Help the circus keeper calculate how many fruits are needed to feed all the animals!</p>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
    <!-- Elephants Section -->
    <div class="bg-gray-50 p-4 rounded-lg shadow-md">
      <div class="bg-blue-200 p-2 rounded-t-lg font-bold text-blue-800 text-center">Elephants</div>
      <div class="p-4">
        <div class="flex justify-center mb-2">
          <div class="text-5xl">🐘 🐘</div>
        </div>
        <div class="grid grid-cols-2 gap-4 mt-4">
          <div class="bg-blue-100 p-3 rounded-lg text-center">
            <div class="text-sm text-blue-700 font-bold">Number of Elephants</div>
            <div class="text-2xl font-bold text-blue-800 mt-1">2</div>
            <div class="text-xs text-blue-600 mt-1">elephants = 2</div>
          </div>
          <div class="bg-blue-100 p-3 rounded-lg text-center">
            <div class="text-sm text-blue-700 font-bold">Fruits per Elephant</div>
            <div class="text-2xl font-bold text-blue-800 mt-1">5</div>
            <div class="text-xs text-blue-600 mt-1">elephant_fruits = 5</div>
          </div>
        </div>
        <div class="bg-blue-50 p-2 rounded-lg mt-3 text-center">
          <div class="text-sm text-blue-700">Total Elephant Fruits</div>
          <div class="text-lg font-bold text-blue-800">elephants × elephant_fruits</div>
          <div class="text-lg font-bold text-blue-800">2 × 5 = 10</div>
        </div>
      </div>
    </div>

    <!-- Monkeys Section -->
    <div class="bg-gray-50 p-4 rounded-lg shadow-md">
      <div class="bg-green-200 p-2 rounded-t-lg font-bold text-green-800 text-center">Monkeys</div>
      <div class="p-4">
        <div class="flex justify-center mb-2">
          <div class="text-4xl">🐒 🐒 🐒 🐒</div>
        </div>
        <div class="grid grid-cols-2 gap-4 mt-4">
          <div class="bg-green-100 p-3 rounded-lg text-center">
            <div class="text-sm text-green-700 font-bold">Number of Monkeys</div>
            <div class="text-2xl font-bold text-green-800 mt-1">4</div>
            <div class="text-xs text-green-600 mt-1">monkeys = 4</div>
          </div>
          <div class="bg-green-100 p-3 rounded-lg text-center">
            <div class="text-sm text-green-700 font-bold">Fruits per Monkey</div>
            <div class="text-2xl font-bold text-green-800 mt-1">3</div>
            <div class="text-xs text-green-600 mt-1">monkey_fruits = 3</div>
          </div>
        </div>
        <div class="bg-green-50 p-2 rounded-lg mt-3 text-center">
          <div class="text-sm text-green-700">Total Monkey Fruits</div>
          <div class="text-lg font-bold text-green-800">monkeys × monkey_fruits</div>
          <div class="text-lg font-bold text-green-800">4 × 3 = 12</div>
        </div>
      </div>
    </div>
  </div>

  <!-- Total Calculation -->
  <div class="bg-purple-100 p-4 rounded-lg shadow-md text-center mb-6">
    <div class="bg-purple-200 p-2 rounded-t-lg font-bold text-purple-800">Total Fruits Needed</div>
    <div class="p-4">
      <div class="flex items-center justify-center gap-3 flex-wrap">
        <div class="bg-blue-100 px-3 py-2 rounded-lg">
          <span class="font-bold text-blue-800">Elephant Fruits</span>
          <div class="text-lg">(elephants × elephant_fruits)</div>
          <div class="text-lg">(2 × 5 = 10)</div>
        </div>
        <div class="text-2xl font-bold text-purple-800">+</div>
        <div class="bg-green-100 px-3 py-2 rounded-lg">
          <span class="font-bold text-green-800">Monkey Fruits</span>
          <div class="text-lg">(monkeys × monkey_fruits)</div>
          <div class="text-lg">(4 × 3 = 12)</div>
        </div>
        <div class="text-2xl font-bold text-purple-800">=</div>
        <div class="bg-purple-200 px-3 py-2 rounded-lg border-2 border-dashed border-purple-500">
          <span class="font-bold text-purple-800">Total Fruits</span>
          <div class="text-lg">10 + 12 = 22</div>
          <div class="text-sm text-purple-600">Store in 'total_fruits'</div>
        </div>
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
      <p>💡 <strong>Hint:</strong> In Python, we can use variables in our calculations! First, calculate how many fruits each type of animal needs by multiplying: elephants * elephant_fruits and monkeys * monkey_fruits. Then, add these results together to get the total: total_fruits = (elephants * elephant_fruits) + (monkeys * monkey_fruits). The parentheses () help us organize our calculation and make it clear!</p>
    </div>
  {/if}
</div>