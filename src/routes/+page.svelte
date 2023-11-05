<script>
	// Import the functions you need from the SDKs you need
	import { goto } from '$app/navigation';
	import { signInWithPopup, signInWithEmailAndPassword, signInAnonymously, createUserWithEmailAndPassword } from 'firebase/auth';
	import { base } from '$app/paths';

	import { auth, provider } from '../util.js';
	import { anonymousMode } from '../store.js';

	let uid = '';
	let loggedIn = false;

	let signUpPage = false;
	let email = '';
	let password = '';

	auth.onAuthStateChanged(async (user) => {
		loggedIn = user ? true : false;
		if (loggedIn) {
			uid = user.uid;
			goto(`${base}/dashboard`);
		} else {
			uid = undefined;
		}
	});

	function userpassLogin() {
		signInWithEmailAndPassword(auth, email, password);
	}

	function googleLogin() {
		signInWithPopup(auth, provider);
	}

	function anonymousLogin() {
		signInAnonymously(auth);
		$anonymousMode = true;
	}
</script>

<h1>Title</h1>
<div id="parent">
	{#if signUpPage}
		<div class="kid">
			<a
				href={base}
				on:click={() => {
					signUpPage = false;
				}}>Return to other sign in options</a
			>
			<br />
			<div class="signup-email"><input bind:value={email} placeholder="Email" /></div>
			<br />
			<input type="password" bind:value={password} placeholder="Password" />
			<br />
			<!-- <Button on:click={createUserWithEmailAndPassword(auth, email, password)}>Sign Up</Button> -->
			<button on:click={createUserWithEmailAndPassword(auth, email, password)}>Sign Up</button>
		</div>
	{:else}
		<div class="kid">
			<input type="text" bind:value={email} placeholder="Email" />
			<br />
			<input type="password" bind:value={password} placeholder="Password" />
			<br />
			<p>Dont have account <a href={base} on:click={() => (signUpPage = true)}>Sign Up</a></p>
			<br />
			<button on:click={userpassLogin} kind="primary">Sign In</button>
			<hr />
			<div class="google">
				<button on:click={googleLogin}>Continue With Google</button>
			</div>
			<br />
			<button on:click={anonymousLogin}> Skip Sign In </button>
		</div>
	{/if}
</div>

<style>
	.kid {
		background-color: rgb(59, 93, 96);
		padding: 4rem;
		border-radius: 2rem;
	}

	p {
		color: white;
	}

	hr {
		margin-top: 1rem;
		margin-bottom: 1rem;
	}

	.google {
		margin-bottom: 0.25rem;
		background-color: rgb(59, 93, 96);
	}

	#parent {
		display: flex;
		justify-content: center;
	}
	h1 {
		text-align: center;
	}
	.signup-email {
		margin-top: 1rem;
		margin-bottom: 0.25rem;
	}
</style>
