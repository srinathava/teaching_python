import type { Session } from '@auth/core/types';

// See https://kit.svelte.dev/docs/types#app
declare global {
    namespace App {
        // interface Error {}
        interface Locals {
            user: {
                id: string;
                name?: string | null;
                email?: string | null;
                image?: string | null;
            } | null;
        }
        interface PageData {
            session: Session | null;
        }
        // interface Platform {}
    }
}

export {};
