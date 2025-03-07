export interface ValidationParams {
    concept: string;
    expectedOutcome: string;
}

export interface Exercise {
    slug: string;
    sequenceKey: number;
    title: string;
    description: string;
    taskDescription: string;
    initialCode: string;
    solution: string;
    hintText?: string; // Now optional since hints are in content.svelte files
    contentPath: string;
    validationParams: ValidationParams;
}

export interface Lesson {
    slug: string;
    title: string;
    description: string;
    order: number;
    icon?: string;
    exercises: Exercise[];
}

export interface ExercisesData {
    lessons: Lesson[];
}

// Helper function to parse validation params
export function parseValidationParams(params: string | null): ValidationParams | null {
    if (!params) return null;
    try {
        return JSON.parse(params);
    } catch {
        return null;
    }
}