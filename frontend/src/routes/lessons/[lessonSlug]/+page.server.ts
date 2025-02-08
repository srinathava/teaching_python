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

    return {
        title: lesson.title,
        description: lesson.description,
        exercises: lesson.exercises.map(ex => ({
            number: Math.floor(ex.sequenceKey),
            title: ex.title,
            description: ex.description
        }))
    };
}) satisfies PageServerLoad;