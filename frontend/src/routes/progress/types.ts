import type { InferSelectModel } from 'drizzle-orm';
import type { progress } from '$lib/server/db/schema';
import type { Exercise, Lesson, ValidationParams } from '$lib/server/content/types';

// Base type from database schema
export type DBProgress = InferSelectModel<typeof progress>;

// Extended types with progress data
export interface ExerciseWithProgress extends Exercise {
    progress: DBProgress[];
}

export interface LessonWithExercises extends Lesson {
    exercises: ExerciseWithProgress[];
}