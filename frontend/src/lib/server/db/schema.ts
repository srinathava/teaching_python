import { sqliteTable, text, integer, primaryKey } from 'drizzle-orm/sqlite-core';

export const user = sqliteTable('user', {
	id: integer('id').primaryKey(),
	age: integer('age')
});

export const progress = sqliteTable('progress', {
	userId: integer('user_id').references(() => user.id).notNull(),
	exerciseSlug: text('exercise_slug').notNull(),
	completed: integer('completed', { mode: 'boolean' }).notNull().default(false),
	completedAt: integer('completed_at'),
	attempts: integer('attempts').notNull().default(0),
	lastAttemptedCode: text('last_attempted_code')
}, (table) => ({
	pk: primaryKey({ columns: [table.userId, table.exerciseSlug] })
}));

export const achievement = sqliteTable('achievement', {
	id: integer('id').primaryKey(),
	slug: text('slug').notNull().unique(),
	title: text('title').notNull(),
	description: text('description'),
	criteria: text('criteria').notNull() // JSON string of requirements
});

export const userAchievement = sqliteTable('user_achievement', {
	userId: integer('user_id').references(() => user.id).notNull(),
	achievementId: integer('achievement_id').references(() => achievement.id).notNull(),
	unlockedAt: integer('unlocked_at').notNull()
}, (table) => ({
	pk: primaryKey({ columns: [table.userId, table.achievementId] })
}));
