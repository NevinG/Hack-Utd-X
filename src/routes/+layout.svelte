<script>
	import { auth, getData } from '../util.js';

	auth.onAuthStateChanged(function (user) {
		if (user != null) {
			getData();
		} else {
			console.log('error with user auth state change');
		}
	});
</script>

<svelte:head>
	<link
		href="https://fonts.googleapis.com/css?family=Roboto:regular,bold&display=swap"
		rel="stylesheet"
	/>
	<title>Property Prober</title>
</svelte:head>

<slot />

<style lang="scss">
	:global(*) {
		font-family: 'Roboto', sans-serif;
	}
	:global(h1) {
		color: white;
	}
	:global(a) {
		color: white;
		text-decoration: none;
	}
	:global(a:hover) {
		color: white;
		text-decoration: underline;
	}
	:global(p) {
		color: white;
	}
	:global(div) {
		color: white;
		// background-color: rgb(1, 42, 45);
	}
	:global(::placeholder) {
		color: rgb(200, 200, 200);
		opacity: 1;
	}
</style>
