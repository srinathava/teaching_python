<script lang="ts">
  // This component can import other components, use assets, etc.
  import type { Exercise } from '$lib/server/content/types';
  export let exercise: Exercise;
</script>

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