<script lang="ts">
  // This component can import other components, use assets, etc.
  import type { Exercise } from '$lib/server/content/types';
  export let exercise: Exercise;
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

  <!-- Circus tips moved to hint text -->
</div>