<script lang="ts">
  // This component can import other components, use assets, etc.
  import type { Exercise } from '$lib/server/content/types';
  export let exercise: Exercise;
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

  <!-- Circus tips moved to hint text -->
</div>