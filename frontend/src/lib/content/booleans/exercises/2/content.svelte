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
    <h3 class="text-xl font-bold text-purple-800">The Circus Ticket Inspector!</h3>
    <p class="text-gray-700">Help check if visitors have the right tickets for the amazing circus show!</p>
  </div>

  <div class="flex flex-col md:flex-row items-center justify-center gap-6 mb-6">
    <!-- Visitor's Ticket -->
    <div class="bg-yellow-100 p-4 rounded-lg shadow-md text-center">
      <div class="bg-yellow-200 p-2 rounded-t-lg font-bold text-yellow-800">Visitor's Ticket</div>
      <div class="bg-white p-4 rounded-b-lg flex flex-col items-center">
        <div class="text-4xl mb-2">🎟️</div>
        <div class="bg-gradient-to-r from-purple-500 to-pink-500 text-white px-3 py-1 rounded-full font-bold">
          VIP
        </div>
        <div class="text-sm text-yellow-600 mt-2">visitor_ticket = "VIP"</div>
      </div>
    </div>

    <!-- Comparison -->
    <div class="flex flex-col items-center">
      <div class="text-3xl font-bold text-purple-800 my-2">==</div>
      <div class="text-sm text-purple-600">(equal to)</div>
    </div>

    <!-- Required Ticket -->
    <div class="bg-green-100 p-4 rounded-lg shadow-md text-center">
      <div class="bg-green-200 p-2 rounded-t-lg font-bold text-green-800">Required Ticket</div>
      <div class="bg-white p-4 rounded-b-lg flex flex-col items-center">
        <div class="text-4xl mb-2">🎪</div>
        <div class="bg-gradient-to-r from-purple-500 to-pink-500 text-white px-3 py-1 rounded-full font-bold">
          VIP
        </div>
        <div class="text-sm text-green-600 mt-2">required_ticket = "VIP"</div>
      </div>
    </div>

    <!-- Equals Sign -->
    <div class="text-3xl font-bold text-purple-800 my-2">=</div>

    <!-- Result Box -->
    <div class="bg-blue-100 p-4 rounded-lg shadow-md text-center border-2 border-dashed border-blue-500">
      <div class="bg-blue-200 p-2 rounded-t-lg font-bold text-blue-800">Result</div>
      <div class="bg-white p-4 rounded-b-lg flex flex-col items-center">
        <div class="text-2xl font-bold text-blue-800">True</div>
        <div class="text-sm text-blue-600">has_correct_ticket = visitor_ticket == required_ticket</div>
      </div>
    </div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
    <!-- Example 1: Match -->
    <div class="bg-green-50 p-4 rounded-lg shadow-md">
      <h4 class="font-bold text-green-800 mb-2">When Tickets Match:</h4>
      <div class="flex items-center justify-center gap-3">
        <div class="bg-white p-2 rounded-lg text-center">
          <div class="bg-gradient-to-r from-purple-500 to-pink-500 text-white px-2 py-1 rounded-full text-sm font-bold">
            VIP
          </div>
        </div>
        <div class="text-xl font-bold text-green-800">==</div>
        <div class="bg-white p-2 rounded-lg text-center">
          <div class="bg-gradient-to-r from-purple-500 to-pink-500 text-white px-2 py-1 rounded-full text-sm font-bold">
            VIP
          </div>
        </div>
        <div class="text-xl font-bold text-green-800">=</div>
        <div class="bg-white p-2 rounded-lg text-center">
          <div class="text-green-800 font-bold">True</div>
        </div>
      </div>
    </div>

    <!-- Example 2: No Match -->
    <div class="bg-red-50 p-4 rounded-lg shadow-md">
      <h4 class="font-bold text-red-800 mb-2">When Tickets Don't Match:</h4>
      <div class="flex items-center justify-center gap-3">
        <div class="bg-white p-2 rounded-lg text-center">
          <div class="bg-gradient-to-r from-purple-500 to-pink-500 text-white px-2 py-1 rounded-full text-sm font-bold">
            VIP
          </div>
        </div>
        <div class="text-xl font-bold text-red-800">==</div>
        <div class="bg-white p-2 rounded-lg text-center">
          <div class="bg-blue-500 text-white px-2 py-1 rounded-full text-sm font-bold">
            Regular
          </div>
        </div>
        <div class="text-xl font-bold text-red-800">=</div>
        <div class="bg-white p-2 rounded-lg text-center">
          <div class="text-red-800 font-bold">False</div>
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
      <p>💡 <strong>Hint:</strong> Use the == (equal to) operator to compare the visitor's ticket type with the required ticket type. This will give you a boolean value (True or False) that you can store in the 'has_correct_ticket' variable. Remember that strings must match exactly, including capitalization.</p>
    </div>
  {/if}
</div>