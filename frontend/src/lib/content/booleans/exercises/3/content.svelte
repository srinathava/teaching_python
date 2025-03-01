<script lang="ts">
  // This component can import other components, use assets, etc.
  import type { Exercise } from '$lib/server/content/types';
  export let exercise: Exercise;
</script>

<div class="mb-6">
  <div class="text-center mb-4">
    <h3 class="text-xl font-bold text-purple-800">The Thrilling Circus Ride!</h3>
    <p class="text-gray-700">Help check if visitors are eligible for the most exciting ride in the circus!</p>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
    <!-- Age Check -->
    <div class="bg-blue-100 p-4 rounded-lg shadow-md">
      <div class="bg-blue-200 p-2 rounded-t-lg font-bold text-blue-800 text-center">Age Check</div>
      <div class="p-4">
        <div class="flex justify-center mb-2">
          <div class="text-5xl">👧</div>
        </div>
        <div class="grid grid-cols-2 gap-4 mt-4">
          <div class="bg-white p-3 rounded-lg text-center">
            <div class="text-sm text-blue-700 font-bold">Visitor's Age</div>
            <div class="text-2xl font-bold text-blue-800 mt-1">14</div>
            <div class="text-xs text-blue-600 mt-1">visitor_age = 14</div>
          </div>
          <div class="bg-white p-3 rounded-lg text-center">
            <div class="text-sm text-blue-700 font-bold">Minimum Age</div>
            <div class="text-2xl font-bold text-blue-800 mt-1">12</div>
            <div class="text-xs text-blue-600 mt-1">min_age = 12</div>
          </div>
        </div>
        <div class="bg-blue-50 p-2 rounded-lg mt-3 text-center">
          <div class="text-sm text-blue-700">Age Check Result</div>
          <div class="text-lg font-bold text-blue-800">visitor_age &gt;= min_age</div>
          <div class="text-lg font-bold text-blue-800">14 &gt;= 12</div>
          <div class="text-lg font-bold text-green-600">True</div>
        </div>
      </div>
    </div>

    <!-- Height Check -->
    <div class="bg-purple-100 p-4 rounded-lg shadow-md">
      <div class="bg-purple-200 p-2 rounded-t-lg font-bold text-purple-800 text-center">Height Check</div>
      <div class="p-4">
        <div class="flex justify-center mb-2">
          <div class="text-5xl">📏</div>
        </div>
        <div class="grid grid-cols-2 gap-4 mt-4">
          <div class="bg-white p-3 rounded-lg text-center">
            <div class="text-sm text-purple-700 font-bold">Visitor's Height</div>
            <div class="text-2xl font-bold text-purple-800 mt-1">130 cm</div>
            <div class="text-xs text-purple-600 mt-1">visitor_height = 130</div>
          </div>
          <div class="bg-white p-3 rounded-lg text-center">
            <div class="text-sm text-purple-700 font-bold">Minimum Height</div>
            <div class="text-2xl font-bold text-purple-800 mt-1">120 cm</div>
            <div class="text-xs text-purple-600 mt-1">min_height = 120</div>
          </div>
        </div>
        <div class="bg-purple-50 p-2 rounded-lg mt-3 text-center">
          <div class="text-sm text-purple-700">Height Check Result</div>
          <div class="text-lg font-bold text-purple-800">visitor_height &gt;= min_height</div>
          <div class="text-lg font-bold text-purple-800">130 &gt;= 120</div>
          <div class="text-lg font-bold text-green-600">True</div>
        </div>
      </div>
    </div>
  </div>

  <!-- Combined Check -->
  <div class="bg-green-100 p-4 rounded-lg shadow-md text-center mb-6">
    <div class="bg-green-200 p-2 rounded-t-lg font-bold text-green-800">Final Eligibility Check</div>
    <div class="p-4">
      <div class="flex items-center justify-center gap-3 flex-wrap">
        <div class="bg-blue-100 px-3 py-2 rounded-lg">
          <span class="font-bold text-blue-800">Age Check</span>
          <div class="text-lg">(visitor_age &gt;= min_age)</div>
          <div class="text-lg">(14 &gt;= 12)</div>
          <div class="text-lg text-green-600">True</div>
        </div>
        <div class="text-2xl font-bold text-green-800">AND</div>
        <div class="bg-purple-100 px-3 py-2 rounded-lg">
          <span class="font-bold text-purple-800">Height Check</span>
          <div class="text-lg">(visitor_height &gt;= min_height)</div>
          <div class="text-lg">(130 &gt;= 120)</div>
          <div class="text-lg text-green-600">True</div>
        </div>
        <div class="text-2xl font-bold text-green-800">=</div>
        <div class="bg-green-200 px-3 py-2 rounded-lg border-2 border-dashed border-green-500">
          <span class="font-bold text-green-800">Can Ride?</span>
          <div class="text-lg">True AND True</div>
          <div class="text-lg text-green-600">True</div>
          <div class="text-sm text-green-600">Store in 'can_ride'</div>
        </div>
      </div>
    </div>
  </div>

  <div class="bg-yellow-100 p-4 rounded-lg shadow-md mb-6">
    <h4 class="font-bold text-yellow-800 mb-2">Logical Operators in Python:</h4>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
      <div class="bg-white p-2 rounded-lg text-center bg-yellow-50">
        <div class="font-bold text-yellow-800">and</div>
        <div class="text-sm text-yellow-600">True if both conditions are True</div>
        <div class="text-xs text-yellow-700 mt-1">True and True = True</div>
        <div class="text-xs text-yellow-700">True and False = False</div>
      </div>
      <div class="bg-white p-2 rounded-lg text-center">
        <div class="font-bold text-yellow-800">or</div>
        <div class="text-sm text-yellow-600">True if at least one condition is True</div>
        <div class="text-xs text-yellow-700 mt-1">True or False = True</div>
        <div class="text-xs text-yellow-700">False or False = False</div>
      </div>
      <div class="bg-white p-2 rounded-lg text-center">
        <div class="font-bold text-yellow-800">not</div>
        <div class="text-sm text-yellow-600">Inverts a boolean value</div>
        <div class="text-xs text-yellow-700 mt-1">not True = False</div>
        <div class="text-xs text-yellow-700">not False = True</div>
      </div>
    </div>
  </div>

  <!-- Circus tips moved to hint text -->
</div>