import { db } from '$lib/server/db';
import { progress, submission } from '$lib/server/db/schema';
import { json } from '@sveltejs/kit';
import type { RequestHandler } from './$types';
import { eq, sql } from 'drizzle-orm';

// Temporary user ID until we implement auth
const TEMP_USER_ID = 1;

export const POST: RequestHandler = async ({ request }) => {
	const { exerciseSlug, code, isCorrect, feedback } = await request.json();

	try {
		// Record the submission
		await db.insert(submission).values({
			userId: TEMP_USER_ID,
			exerciseSlug,
			code,
			isCorrect,
			feedback,
			createdAt: Date.now()
		});

		if (isCorrect) {
			// Update or insert progress
			await db
				.insert(progress)
				.values({
					userId: TEMP_USER_ID,
					exerciseSlug,
					completed: true,
					completedAt: Date.now(),
					attempts: 1
				})
				.onConflictDoUpdate({
					target: [progress.userId, progress.exerciseSlug],
					set: {
						completed: true,
						completedAt: Date.now(),
						attempts: sql`attempts + 1`
					}
				});
		} else {
			// Just increment attempts if not correct
			await db
				.insert(progress)
				.values({
					userId: TEMP_USER_ID,
					exerciseSlug,
					completed: false,
					attempts: 1
				})
				.onConflictDoUpdate({
					target: [progress.userId, progress.exerciseSlug],
					set: {
						attempts: sql`attempts + 1`
					}
				});
		}

		return json({ success: true });
	} catch (error) {
		console.error('Error updating progress:', error);
		return json({ success: false, error: 'Failed to update progress' }, { status: 500 });
	}
};