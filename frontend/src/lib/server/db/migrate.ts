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
        // List tables before dropping
        const beforeTables = await client.execute(`
            SELECT name FROM sqlite_master WHERE type='table';
        `);
        console.error('Tables before dropping:', beforeTables.rows);

        // Drop existing tables to ensure clean state
        console.error('Dropping tables...');
        await client.execute(`DROP TABLE IF EXISTS user_achievement;`);
        await client.execute(`DROP TABLE IF EXISTS achievement;`);
        await client.execute(`DROP TABLE IF EXISTS progress;`);
        await client.execute(`DROP TABLE IF EXISTS user;`);

        // List tables after dropping
        const afterTables = await client.execute(`
            SELECT name FROM sqlite_master WHERE type='table';
        `);
        console.error('Tables after dropping:', afterTables.rows);

        // Create user table first (no dependencies)
        console.error('Creating user table...');
        await client.execute(`
            CREATE TABLE user (
                id INTEGER PRIMARY KEY,
                age INTEGER
            );
        `);

        // Create progress table (depends on user)
        console.error('Creating progress table...');
        await client.execute(`
            CREATE TABLE progress (
                user_id INTEGER NOT NULL,
                exercise_slug TEXT NOT NULL,
                completed INTEGER NOT NULL DEFAULT 0,
                completed_at INTEGER,
                attempts INTEGER NOT NULL DEFAULT 0,
                last_attempted_code TEXT,
                PRIMARY KEY (user_id, exercise_slug),
                FOREIGN KEY (user_id) REFERENCES user(id)
            );
        `);

        // Create achievement table (no dependencies)
        console.error('Creating achievement table...');
        await client.execute(`
            CREATE TABLE achievement (
                id INTEGER PRIMARY KEY,
                slug TEXT NOT NULL UNIQUE,
                title TEXT NOT NULL,
                description TEXT,
                criteria TEXT NOT NULL
            );
        `);

        // Create user_achievement table (depends on both user and achievement)
        console.error('Creating user_achievement table...');
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