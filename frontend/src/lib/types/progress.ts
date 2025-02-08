export interface Progress {
    exercise_slug: string;
    completed: boolean;
    completed_at: string | null;
    attempts: number;
    last_attempted_code: string | null;
}