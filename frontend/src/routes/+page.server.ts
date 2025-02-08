import { loadExercisesData } from '$lib/server/content/loader';

export function load() {
    const exercisesData = loadExercisesData();
    return {
        lessons: exercisesData.lessons
    };
}