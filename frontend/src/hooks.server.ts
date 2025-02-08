import { env } from '$env/dynamic/private';

// Ensure required environment variables are set
if (!env.DATABASE_URL) {
    throw new Error('DATABASE_URL environment variable is required');
}