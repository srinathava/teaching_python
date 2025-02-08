import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import { loadExercisesData } from '$lib/server/content/loader';

export const load = (async ({ params }) => {
    const data = loadExercisesData();

    // Find the lesson
    const lesson = data.lessons.find(l => l.slug === params.lessonSlug);
    if (!lesson) {
        throw error(404, 'Lesson not found');
    }

    // Find the exercise
    const exerciseIndex = parseInt(params.exerciseNumber) - 1;
    const exercise = lesson.exercises[exerciseIndex];
    if (!exercise) {
        throw error(404, 'Exercise not found');
    }

    return {
        lesson,
        exercise,
        totalExercises: lesson.exercises.length,
        exerciseNumber: exerciseIndex + 1
    };
}) satisfies PageServerLoad;