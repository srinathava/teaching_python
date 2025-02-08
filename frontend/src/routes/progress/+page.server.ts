import { db } from '$lib/server/db';
import { progress } from '$lib/server/db/schema';
import { eq } from 'drizzle-orm';
import type { PageServerLoad } from './$types';
import type { LessonWithExercises, DBProgress } from './types';
import { loadExercisesData } from '$lib/server/content/loader';

// Temporary user ID until we implement auth
const TEMP_USER_ID = 1;

export const load = (async () => {
	const data = loadExercisesData();

	// Get all progress records for the user
	const progressRecords = await db
		.select()
		.from(progress)
		.where(eq(progress.userId, TEMP_USER_ID));

	// Create a map of exercise slug to progress
	const progressMap = new Map<string, DBProgress>();
	for (const record of progressRecords) {
		progressMap.set(record.exerciseSlug, record);
	}

	// Merge progress data with exercises
	const lessonsWithProgress = data.lessons.map(lesson => ({
		...lesson,
		exercises: lesson.exercises.map(ex => ({
			...ex,
			progress: progressMap.has(ex.slug) ? [progressMap.get(ex.slug)!] : []
		}))
	})) as LessonWithExercises[];

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