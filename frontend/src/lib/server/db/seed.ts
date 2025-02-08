import 'dotenv/config';
import { db } from './index.js';
import { user, progress } from './schema.js';
import { eq } from 'drizzle-orm';
import { readFileSync } from 'fs';
import { join } from 'path';
import type { ExercisesData } from '../content/types';
import { fileURLToPath } from 'url';

async function seed() {
    try {
        // Check if test user exists
        const existingUser = await db.select().from(user).where(eq(user.id, 1)).get();
        
        if (!existingUser) {
            // Create test user if it doesn't exist
            const [testUser] = await db
                .insert(user)
                .values({
                    id: 1, // This matches our TEMP_USER_ID
                    age: 10
                })
                .returning();

            console.log('Created test user:', testUser);
        } else {
            console.log('Test user already exists');
        }

        // Load exercises data
        const filePath = join(process.cwd(), 'src/lib/server/content/exercises.json');
        const content = readFileSync(filePath, 'utf-8');
        const exercisesData: ExercisesData = JSON.parse(content);

        // Create initial progress records for each exercise
        for (const lesson of exercisesData.lessons) {
            for (const exercise of lesson.exercises) {
                try {
                    await db.insert(progress).values({
                        userId: 1,
                        exerciseSlug: exercise.slug,
                        completed: false,
                        attempts: 0
                    }).onConflictDoNothing();
                } catch (error) {
                    console.error(`Error creating progress for exercise ${exercise.slug}:`, error);
                }
            }
        }

        console.log('Seed data inserted successfully');
    } catch (error) {
        console.error('Error seeding data:', error);
        throw error;
    }
}

// Only run seeding if this file is executed directly
if (process.argv[1] === fileURLToPath(import.meta.url)) {
    seed()
        .then(() => process.exit(0))
        .catch((error) => {
            console.error(error);
            process.exit(1);
        });
}

// Export for use in tests or other modules
export { seed };