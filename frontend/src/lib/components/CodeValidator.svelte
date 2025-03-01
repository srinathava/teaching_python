<script lang="ts">
	import { fade } from 'svelte/transition';
	import { goto } from '$app/navigation';
	
	export let lessonId: string;
	export let exerciseId: string;
	export let code: string;
	export let concept: string;
	export let exerciseDescription: string | undefined = undefined;
	export let expectedOutcome: string | undefined = undefined;
	export let nextExercise: string | null = null;
	export let session: any;

	type ValidationResult = {
		success: boolean;
		message: string;
		hints?: string[];
		errorLine?: number;
		errorColumn?: number;
	};

	let feedback: ValidationResult | null = null;
	let isValidating = false;

	async function validateCode(): Promise<ValidationResult> {
		const response = await fetch('/api/validate', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({
				code,
				exercise_id: exerciseId,
				concept,
				exercise_description: exerciseDescription,
				expected_outcome: expectedOutcome
			})
		});
		
		if (!response.ok) {
			throw new Error('Failed to validate code');
		}
		
		return response.json();
	}

	async function updateProgress(result: ValidationResult) {
		try {
			const response = await fetch('/api/progress', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({
					exercise_slug: exerciseId,
					code,
					is_correct: result.success,
					user_id: session?.user?.id
				})
			});

			if (!response.ok) {
				console.error('Failed to update progress');
			}
		} catch (error) {
			console.error('Error updating progress:', error);
		}
	}

	async function handleValidation() {
		isValidating = true;
		feedback = null;
		
		try {
			const result = await validateCode();
			feedback = result;
			
			// Update progress regardless of success/failure
			await updateProgress(result);
		} catch (error) {
			console.error('Code validation error:', error);
			feedback = {
				success: false,
				message: "Oops! Something went wrong. Please try again later!",
			};
		} finally {
			isValidating = false;
		}
	}
</script>

<!-- Run Code Button -->
<button 
	class="px-4 py-2 bg-green-500 hover:bg-green-600 text-white rounded-lg transition-colors flex items-center space-x-2"
	on:click={handleValidation}
	disabled={isValidating}
>
	{#if isValidating}
		<svg class="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
			<circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
			<path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
		</svg>
		<span>Validating...</span>
	{:else}
		<span>Run Code</span>
	{/if}
</button>

<!-- Feedback Display -->
{#if feedback}
	<div 
		class="mt-4 p-4 rounded-lg" 
		class:bg-green-50={feedback.success}
		class:bg-red-50={!feedback.success}
		transition:fade
	>
		<!-- Main Message -->
		<p class="font-medium" class:text-green-800={feedback.success} class:text-red-800={!feedback.success}>
			{feedback.message}
		</p>
		
		<!-- Additional Hints -->
		{#if feedback.hints && feedback.hints.length > 0}
			<ul class="mt-2 space-y-1">
				{#each feedback.hints as hint}
					<li class="text-sm text-gray-600">💡 {hint}</li>
				{/each}
			</ul>
		{/if}
		
		<!-- Error Location -->
		{#if feedback.errorLine !== undefined && feedback.errorColumn !== undefined}
			<p class="mt-2 text-sm text-gray-600">
				Error location: Line {feedback.errorLine}, Column {feedback.errorColumn}
			</p>
		{/if}

		<!-- Next Exercise Button -->
		{#if feedback.success && nextExercise}
			<div class="mt-4">
				<button 
					class="px-4 py-2 bg-blue-500 hover:bg-blue-600 text-white rounded-lg transition-colors"
					on:click={() => goto(nextExercise)}
				>
					Next Exercise →
				</button>
			</div>
		{/if}
	</div>
{/if}