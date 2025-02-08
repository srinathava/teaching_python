<script lang="ts">
  import ExerciseTemplate from '$lib/components/ExerciseTemplate.svelte';
  import type { PageData } from './$types';

  export let data: PageData;

  const lessonPath = `/lessons/${data.lesson.slug}`;
</script>

<ExerciseTemplate
  exercise={data.exercise}
  {lessonPath}
  exerciseNumber={data.exerciseNumber}
  totalExercises={data.totalExercises}
/>