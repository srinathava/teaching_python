import { env } from '$env/dynamic/private';
import { SvelteKitAuth } from '@auth/sveltekit';
import Google from '@auth/core/providers/google';
import type { Session } from '@auth/core/types';
import type { Handle } from '@sveltejs/kit';

// Ensure required environment variables are set
if (!env.DATABASE_URL) {
    throw new Error('DATABASE_URL environment variable is required');
}

if (!env.GOOGLE_CLIENT_ID || !env.GOOGLE_CLIENT_SECRET) {
    throw new Error('Google OAuth credentials are required');
}

if (!env.AUTH_SECRET) {
    throw new Error('AUTH_SECRET environment variable is required');
}

// After our checks above, we can safely assert these are strings
const GOOGLE_CLIENT_ID = env.GOOGLE_CLIENT_ID as string;
const GOOGLE_CLIENT_SECRET = env.GOOGLE_CLIENT_SECRET as string;
const AUTH_SECRET = env.AUTH_SECRET as string;

// Create the auth handler
const auth = SvelteKitAuth({
    providers: [
        Google({
            clientId: GOOGLE_CLIENT_ID,
            clientSecret: GOOGLE_CLIENT_SECRET,
            authorization: {
                params: {
                    prompt: "consent",
                    access_type: "offline",
                    response_type: "code"
                }
            }
        })
    ],
    secret: AUTH_SECRET,
    trustHost: true,
    callbacks: {
        async session({ session, token }): Promise<Session> {
            if (session?.user && token?.sub) {
                session.user.id = token.sub;
            }
            return session;
        },
        async jwt({ token, user }) {
            if (user) {
                token.sub = user.id;
            }
            return token;
        }
    }
});

// Export the handle function from the auth handler
export const handle: Handle = auth.handle;