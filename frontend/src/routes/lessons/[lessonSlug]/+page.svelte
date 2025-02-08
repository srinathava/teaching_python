<script lang="ts">
  import { float } from '$lib/transitions';
  import { goto } from '$app/navigation';
  import type { PageData } from './$types';
  import { page } from '$app/stores';

  export let data: PageData;

  function startExercise(number: number) {
    goto(`/lessons/${$page.params.lessonSlug}/exercises/${number}`);
  }
</script>

<div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
  <div class="bg-white rounded-lg shadow-lg p-6" in:float={{ y: 5, duration: 1000 }}>
    <h1 class="text-3xl font-bold text-gray-900 mb-4">{data.title}</h1>
    <p class="text-gray-600 mb-8">{data.description}</p>

    <div class="space-y-4">
      {#each data.exercises as exercise (exercise.number)}
        <button
          class="w-full p-4 bg-blue-50 hover:bg-blue-100 rounded-lg transition-colors flex items-center justify-between group"
          on:click={() => startExercise(exercise.number)}
        >
          <div>
            <h3 class="text-lg font-semibold text-blue-900 group-hover:text-blue-700 flex items-center gap-2">
              <span class="text-sm px-2 py-0.5 bg-blue-100 text-blue-700 rounded">{exercise.number}</span>
              {exercise.title}
            </h3>
            <p class="text-blue-600 group-hover:text-blue-500">{exercise.description}</p>
          </div>
          <svg
            class="w-6 h-6 text-blue-500 group-hover:text-blue-600 transform group-hover:translate-x-1 transition-transform"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M9 5l7 7-7 7"
            />
          </svg>
        </button>
      {/each}
    </div>
  </div>
</div>