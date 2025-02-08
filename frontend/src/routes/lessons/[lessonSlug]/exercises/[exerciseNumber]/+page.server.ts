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

    // Find the exercise by sequenceKey
    const sequenceKey = parseFloat(params.exerciseNumber);
    const exercise = lesson.exercises.find(e => e.sequenceKey === sequenceKey);
    if (!exercise) {
        throw error(404, 'Exercise not found');
    }

    // Calculate exercise number based on sorted sequence keys
    const sortedExercises = [...lesson.exercises].sort((a, b) => a.sequenceKey - b.sequenceKey);
    const exerciseNumber = sortedExercises.findIndex(e => e.sequenceKey === sequenceKey) + 1;

    return {
        lesson,
        exercise,
        totalExercises: lesson.exercises.length,
        exerciseNumber
    };
}) satisfies PageServerLoad;