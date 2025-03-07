import { error, redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import { loadExercisesData } from '$lib/server/content/loader';
import type { Progress } from '$lib/types/progress';

export const load = (async ({ params, fetch, locals }) => {
    // Require authentication
    const session = await locals.getSession();
    if (!session?.user) {
        throw redirect(303, '/');
    }

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

    // Fetch user's progress from Python backend using authenticated user's ID
    let userProgress: Progress | undefined;
    try {
        const progressResponse = await fetch(`/api/progress/${session.user.id}`);
        if (progressResponse.ok) {
            const { progress: progressRecords } = await progressResponse.json() as { progress: Progress[] };
            userProgress = progressRecords.find(p => p.exercise_slug === exercise.slug);
        }
    } catch (error) {
        console.error('Failed to fetch progress:', error);
    }

    // Transform snake_case to camelCase for frontend consumption
    const transformedProgress = userProgress ? {
        completed: userProgress.completed,
        attempts: userProgress.attempts,
        completedAt: userProgress.completed_at ? new Date(userProgress.completed_at).getTime() : null,
        lastAttemptedCode: userProgress.last_attempted_code
    } : {
        completed: false,
        attempts: 0,
        completedAt: null,
        lastAttemptedCode: null
    };

    return {
        lesson,
        exercise,
        totalExercises: lesson.exercises.length,
        exerciseNumber,
        progress: transformedProgress,
        session
    };
}) satisfies PageServerLoad;