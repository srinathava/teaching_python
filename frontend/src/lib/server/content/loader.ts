import { readFileSync } from 'fs';
import { join } from 'path';
import type { ExercisesData } from './types';

// Initialize cache with data
const filePath = join(process.cwd(), 'src/lib/server/content/exercises.json');
const content = readFileSync(filePath, 'utf-8');
const cachedData: ExercisesData = JSON.parse(content);

export function loadExercisesData(): ExercisesData {
    return cachedData;
}