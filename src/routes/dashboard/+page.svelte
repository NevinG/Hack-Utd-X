<script>
	import { signOut } from 'firebase/auth';
	import { auth } from '../../util.js';
	import { goto } from '$app/navigation';
	import { userData } from '../../store.js';
	import '../../app.postcss';

	function logout() {
		signOut(auth);
		goto('/');
	}
</script>

<div class="w-screen h-screen flex items-center justify-center bg-slate-600">
	<div>
		<h1 class="text-3xl">Properties:</h1>
		{#each $userData['properties'] as property, i}
			<a class="block p-2 rounded-md bg-slate-500 text-white mb-3" href="/dashboard/{i}"
				>{property.name}</a
			>
		{/each}
	</div>
</div>

<button on:click={logout}>logout</button>

<style>
</style>
