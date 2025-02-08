import { drizzle } from 'drizzle-orm/libsql';
import { createClient } from '@libsql/client';
import * as schema from './schema';

// Try SvelteKit's env first, fall back to process.env for seeding
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

const client = createClient({
    url: databaseUrl,
    authToken: "ignored" // Required by libsql even for file databases
});

// Pass the schema to drizzle to enable proper typing
export const db = drizzle(client, { schema });

// Export schema for use in other files
export { schema };
