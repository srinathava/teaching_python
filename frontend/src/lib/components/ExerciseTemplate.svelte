<script lang="ts">
  import { float } from '$lib/transitions';
  import { fade } from 'svelte/transition';
  import { goto } from '$app/navigation';
  import CodeValidator from '$lib/components/CodeValidator.svelte';
  import MonacoEditor from '$lib/components/MonacoEditor.svelte';
  import { onMount } from 'svelte';
  import type { Exercise } from '$lib/server/content/types';

  // Define the glob pattern for all exercise content components
  const exerciseModules = import.meta.glob('$lib/content/**/content.svelte');

  export let exercise: Exercise;
  export let exerciseNumber: number;
  export let totalExercises: number;
  export let progress: {
    completed: boolean;
    attempts: number;
    completedAt: number | null;
    lastAttemptedCode: string | null;
  };
  
  let codeInput = progress.lastAttemptedCode || exercise.initialCode;
  let showHint = false;
  let ExerciseContent: any = null;
  
  onMount(async () => {
    try {
      // Get the module loader function for this exercise's content path
      const moduleLoader = exerciseModules[`/src/lib/content/${exercise.contentPath}`];
      if (!moduleLoader) {
        throw new Error(`No module found for path: ${exercise.contentPath}`);
      }
      
      // Load and get the default export
      const module = await moduleLoader() as { default: any };
      ExerciseContent = module.default;
    } catch (error) {
      console.error('Failed to load exercise content:', error);
    }
  });
  
  function toggleHint() {
    showHint = !showHint;
  }
  
  function goBack() {
    goto('/');
  }

  function handleCodeChange(event: CustomEvent<string>) {
    codeInput = event.detail;
  }
</script>

<div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
  <!-- Exercise Header -->
  <div class="flex items-center justify-between mb-8">
    <button 
      class="flex items-center text-blue-600 hover:text-blue-800"
      on:click={goBack}
    >
      <span class="mr-2">←</span>
      Back to Lessons
    </button>
    <span class="text-sm font-medium text-gray-500">Exercise {exerciseNumber} of {totalExercises}</span>
  </div>

  <!-- Exercise Content -->
  <div class="bg-white rounded-lg shadow-lg p-6" in:float={{ y: 5, duration: 1000 }}>
    <h1 class="text-3xl font-bold text-gray-900 mb-4">{exercise.title}</h1>
    <p class="text-gray-600 mb-6">{exercise.description}</p>

    <!-- Dynamic Exercise Content -->
    {#if ExerciseContent}
      <svelte:component this={ExerciseContent} {exercise} />
    {:else}
      <div class="animate-pulse bg-gray-100 h-40 rounded-lg mb-6"></div>
    {/if}

    <!-- Task Description -->
    <div class="bg-gray-50 p-4 rounded-lg mb-6">
      <p class="font-semibold text-gray-700">{exercise.taskDescription}</p>
    </div>

    <!-- Code Editor -->
    <div class="mb-6">
      <MonacoEditor
        value={codeInput}
        language="python"
        height="200px"
        on:change={handleCodeChange}
      />
    </div>

    <!-- Controls -->
    <div class="flex justify-between items-center">
      <CodeValidator
        lessonId={exercise.validationParams.concept}
        exerciseId={exercise.slug}
        code={codeInput}
        concept={exercise.validationParams.concept}
        exerciseDescription={`${exercise.description} ${exercise.taskDescription}`}
        expectedOutcome={exercise.validationParams.expectedOutcome}
        nextExercise={null}
      />
      <button 
        class="px-4 py-2 bg-yellow-500 hover:bg-yellow-600 text-white rounded-lg transition-colors"
        on:click={toggleHint}
      >
        {showHint ? 'Hide Hint' : 'Show Hint'}
      </button>
    </div>

    <!-- Hint Area -->
    {#if showHint}
      <div class="mt-4 p-4 bg-yellow-50 text-yellow-800 rounded-lg" transition:fade>
        💡 Hint: {exercise.hintText}
      </div>
    {/if}
  </div>
</div>