<script lang="ts">
  import { onMount } from 'svelte';
  import { float } from '$lib/transitions';
  
  export let data;
  let mounted = false;
  
  onMount(() => {
    mounted = true;
  });
</script>

<div class="min-h-screen bg-gradient-to-b from-blue-50 to-white">
  <div class="max-w-3xl mx-auto px-4 py-12">
    {#if mounted}
      <div class="text-center mb-12" in:float={{y: 20, duration: 800}}>
        <h1 class="text-4xl font-extrabold text-text-dark font-comic-neue mb-4">
          Learn Python!
        </h1>
        <p class="text-lg text-gray-600">
          Choose an exercise below to start your coding adventure
        </p>
      </div>

      <div class="space-y-8">
        {#each data.lessons as lesson}
          <div class="bg-white rounded-lg shadow-sm p-6">
            <!-- Lesson Header -->
            <div class="flex items-center mb-4">
              <span class="text-3xl mr-4">
                {lesson.icon || '📚'}
              </span>
              <div>
                <h2 class="text-2xl font-comic-neue font-bold text-text-dark">
                  {lesson.title}
                </h2>
                <p class="text-gray-600 mt-1">
                  {lesson.description}
                </p>
              </div>
            </div>

            <!-- Exercises -->
            <div class="ml-12 space-y-4 mt-6">
              {#each lesson.exercises as exercise}
                <a 
                  href="/lessons/{lesson.slug}/exercises/{exercise.sequenceKey}"
                  class="block bg-blue-50 p-4 rounded-lg hover:bg-blue-100 transition-colors"
                >
                  <h3 class="text-lg font-comic-neue font-bold text-text-dark flex items-center">
                    <span class="text-xl mr-2">
                      {#if exercise.sequenceKey === 1.0}1️⃣
                      {:else if exercise.sequenceKey === 2.0}2️⃣
                      {:else}🎯{/if}
                    </span>
                    {exercise.title}
                  </h3>
                  <p class="text-gray-600 mt-1 ml-8">
                    {exercise.description}
                  </p>
                </a>
              {/each}
            </div>
          </div>
        {/each}
      </div>
    {/if}
  </div>
</div>
