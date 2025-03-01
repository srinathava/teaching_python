<script lang="ts">
  // This component can import other components, use assets, etc.
  import type { Exercise } from '$lib/server/content/types';
  export let exercise: Exercise;
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

  <!-- Circus tips moved to hint text -->
</div>