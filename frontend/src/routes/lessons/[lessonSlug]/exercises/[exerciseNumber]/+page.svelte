<script lang="ts">
  import ExerciseTemplate from '$lib/components/ExerciseTemplate.svelte';
  import type { PageData } from './$types';

  export let data: PageData;
</script>

<ExerciseTemplate
  exercise={data.exercise}
  exerciseNumber={data.exerciseNumber}
  totalExercises={data.totalExercises}
/>