import 'dotenv/config';
import { createClient } from '@libsql/client';
import { drizzle } from 'drizzle-orm/libsql';
import { migrate } from 'drizzle-orm/libsql/migrator';
import * as schema from './schema';

// Try SvelteKit's env first, fall back to process.env for migrations
let databaseUrl: string;

if (process.env.DATABASE_URL) {
    databaseUrl = process.env.DATABASE_URL;
} else {
    try {
        const { DATABASE_URL } = await import('$env/static/private');
        databaseUrl = DATABASE_URL;
    } catch {
        throw new Error('DATABASE_URL is not set');
    }
}

async function runMigration() {
    console.error('Database URL:', databaseUrl);
    console.error('Current working directory:', process.cwd());
    
    // Create the database file if it doesn't exist
    const client = createClient({ 
        url: databaseUrl,
        authToken: "ignored" // Required by libsql even for file databases
    });

    // Verify the database connection
    try {
        await client.execute('SELECT 1');
        console.error('Database connection successful');
    } catch (error) {
        console.error('Database connection failed:', error);
        throw error;
    }

    const db = drizzle(client, { schema });

    console.error('Running migrations...');
    try {
        // Drop existing tables to ensure clean state
        await client.execute(`
            DROP TABLE IF EXISTS user_achievement;
            DROP TABLE IF EXISTS achievement;
            DROP TABLE IF EXISTS progress;
            DROP TABLE IF EXISTS user;
        `);

        // Create tables
        await client.execute(`
            CREATE TABLE user (
                id INTEGER PRIMARY KEY,
                age INTEGER
            );
        `);

        await client.execute(`
            CREATE TABLE progress (
                user_id INTEGER NOT NULL,
                exercise_slug TEXT NOT NULL,
                completed INTEGER NOT NULL DEFAULT 0,
                completed_at INTEGER,
                attempts INTEGER NOT NULL DEFAULT 0,
                PRIMARY KEY (user_id, exercise_slug),
                FOREIGN KEY (user_id) REFERENCES user(id)
            );
        `);

        await client.execute(`
            CREATE TABLE achievement (
                id INTEGER PRIMARY KEY,
                slug TEXT NOT NULL UNIQUE,
                title TEXT NOT NULL,
                description TEXT,
                criteria TEXT NOT NULL
            );
        `);

        await client.execute(`
            CREATE TABLE user_achievement (
                user_id INTEGER NOT NULL,
                achievement_id INTEGER NOT NULL,
                unlocked_at INTEGER NOT NULL,
                PRIMARY KEY (user_id, achievement_id),
                FOREIGN KEY (user_id) REFERENCES user(id),
                FOREIGN KEY (achievement_id) REFERENCES achievement(id)
            );
        `);

        // Verify the schema
        const tables = await client.execute(`
            SELECT name, sql FROM sqlite_master WHERE type='table';
        `);
        console.error('All tables and their schemas:', tables.rows);

        // Verify the progress table specifically
        const progressTable = await client.execute(`
            PRAGMA table_info(progress);
        `);
        console.error('Progress table columns:', progressTable.rows);

        console.error('Migrations completed successfully');
    } catch (error) {
        console.error('Migration failed:', error);
        throw error;
    } finally {
        await client.close();
    }
}

runMigration().catch((error) => {
    console.error('Migration failed:', error);
    process.exit(1);
});