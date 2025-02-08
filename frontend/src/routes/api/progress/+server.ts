// This endpoint has been moved to the Python backend.
// The file is kept temporarily to document the change.
// TODO: Remove this file once the migration is complete and tested.

import { error } from '@sveltejs/kit';

export const POST = async () => {
    throw error(404, 'This endpoint has been moved to the Python backend');
};