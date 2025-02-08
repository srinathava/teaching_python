<script lang="ts">
	import { goto } from '$app/navigation';
	import type { PageData } from './$types';
	import type { Exercise, Lesson } from '$lib/server/content/types';

	export let data: PageData;

	function startExercise(lesson: Lesson, exercise: Exercise) {
		goto(`/lessons/${lesson.slug}/exercises/${Math.floor(exercise.sequenceKey)}`);
	}
</script>

<div class="mx-auto max-w-7xl px-4 py-16 sm:px-6 lg:px-8">
	<div class="text-center">
		<h1
			class="font-comic-neue text-4xl font-extrabold tracking-tight text-text-dark sm:text-5xl md:text-6xl"
		>
			Your Progress
		</h1>
		<p
			class="mx-auto mt-3 max-w-md text-base text-gray-500 sm:text-lg md:mt-5 md:max-w-3xl md:text-xl"
		>
			Track your Python learning journey!
		</p>
	</div>

	<!-- Overall Progress -->
	<div class="mt-10">
		<div class="mb-4 flex items-center justify-between">
			<h2 class="text-xl font-semibold">Overall Progress</h2>
			<span class="text-lg font-medium text-gray-600"
				>{data.stats.completedExercises} / {data.stats.totalExercises} Exercises</span
			>
		</div>
		<div class="h-4 w-full overflow-hidden rounded-full bg-gray-200">
			<div
				class="h-full rounded-full bg-green-500 transition-all duration-500"
				style="width: {data.stats.progressPercentage}%"
			/>
		</div>
		<p class="mt-2 text-center text-sm text-gray-600">
			{data.stats.progressPercentage}% Complete
		</p>
	</div>

	<!-- Lessons List -->
	<div class="mt-12 space-y-8">
		{#each data.lessons as lesson}
			<div class="overflow-hidden rounded-lg bg-white shadow">
				<div class="px-4 py-5 sm:p-6">
					<div class="flex items-center justify-between">
						<h3 class="text-lg font-medium leading-6 text-gray-900">
							{lesson.title}
						</h3>
						<span class="text-sm text-gray-500"
							>{lesson.exercises.filter((ex) => ex.progress?.[0]?.completed).length} /
							{lesson.exercises.length} Complete</span
						>
					</div>
					{#if lesson.description}
						<p class="mt-1 text-sm text-gray-500">
							{lesson.description}
						</p>
					{/if}

					<!-- Exercise List -->
					<div class="mt-4 space-y-3">
						{#each lesson.exercises as exercise}
							<button
								class="w-full flex items-center justify-between rounded-md border border-gray-200 p-3 hover:bg-gray-50 transition-colors"
								on:click={() => startExercise(lesson, exercise)}
							>
								<div class="text-left">
									<h4 class="font-medium text-gray-900">{exercise.title}</h4>
									{#if exercise.description}
										<p class="text-sm text-gray-500">
											{exercise.description}
										</p>
									{/if}
								</div>
								{#if exercise.progress?.[0]?.completed}
									<span
										class="inline-flex items-center rounded-full bg-green-100 px-3 py-0.5 text-sm font-medium text-green-800"
									>
										Completed
									</span>
								{:else}
									<span
										class="inline-flex items-center rounded-full bg-blue-100 px-3 py-0.5 text-sm font-medium text-blue-800"
									>
										Start
									</span>
								{/if}
							</button>
						{/each}
					</div>
				</div>
			</div>
		{/each}
	</div>
</div>