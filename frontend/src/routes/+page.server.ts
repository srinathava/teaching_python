import type { PageServerLoad } from './$types';
import type { Progress } from '$lib/types/progress';
import { loadExercisesData } from '$lib/server/content/loader';
import { redirect } from '@sveltejs/kit';

export const load = (async ({ fetch, locals }) => {
    const data = loadExercisesData();

    // Only fetch progress if user is authenticated
    const session = await locals.getSession();
    if (session?.user?.id) {
        const progressResponse = await fetch(`/api/progress/${session.user.id}`);
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
    }

    // Return basic lesson data without progress for unauthenticated users
    return {
        lessons: data.lessons.map(lesson => ({
            ...lesson,
            exercises: lesson.exercises.map(ex => ({
                ...ex,
                progress: []
            }))
        })),
        stats: {
            totalExercises: 0,
            completedExercises: 0,
            progressPercentage: 0
        }
    };
}) satisfies PageServerLoad;