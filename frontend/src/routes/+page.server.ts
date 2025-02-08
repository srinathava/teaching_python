import type { PageServerLoad } from './$types';
import type { Progress } from '$lib/types/progress';
import { loadExercisesData } from '$lib/server/content/loader';

// Temporary user ID until we implement auth
const TEMP_USER_ID = 1;

export const load = (async ({ fetch }) => {
    const data = loadExercisesData();

    // Fetch progress data from Python backend
    const progressResponse = await fetch(`/api/progress/${TEMP_USER_ID}`);
    if (!progressResponse.ok) {
        console.error('Failed to fetch progress data');
        throw new Error('Failed to fetch progress data');
    }

    const { progress: progressRecords } = await progressResponse.json() as { progress: Progress[] };

    // Create a map of exercise slug to progress
    const progressMap = new Map<string, Progress>();
    for (const record of progressRecords) {
        progressMap.set(record.exercise_slug, record);
    }

    // Merge progress data with exercises
    const lessonsWithProgress = data.lessons.map(lesson => ({
        ...lesson,
        exercises: lesson.exercises.map(ex => ({
            ...ex,
            progress: progressMap.has(ex.slug) ? [progressMap.get(ex.slug)!] : []
        }))
    }));

    // Calculate completion stats
    const totalExercises = lessonsWithProgress.reduce(
        (sum, lesson) => sum + lesson.exercises.length,
        0
    );
    const completedExercises = lessonsWithProgress.reduce(
        (sum, lesson) =>
            sum +
            lesson.exercises.filter(ex => ex.progress?.[0]?.completed)
                .length,
        0
    );

    return {
        lessons: lessonsWithProgress,
        stats: {
            totalExercises,
            completedExercises,
            progressPercentage: totalExercises
                ? Math.round((completedExercises / totalExercises) * 100)
                : 0
        }
    };
}) satisfies PageServerLoad;