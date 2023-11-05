import { error } from '@sveltejs/kit';
/** @type {import('./$types').PageLoad} */
export function load({ params }) {
	if (params.id) {
		const number = parseInt(params.id);
		return { id: number };
	}
	throw error(404, 'Not found');
}
