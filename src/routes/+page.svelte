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

<h1>PropertyProber</h1>
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
			<div class = "center-text"
			<p>Don't have an account <a href={base} on:click={() => (signUpPage = true)} style="text-decoration: underline;">Sign Up</a><p>
			</div>
			<br />
			<button on:click={userpassLogin} kind="primary">Sign In</button>
			<hr />
			<div class="google">
				<button on:click={googleLogin}>Continue With Google</button>
			</div>
			<br />
			<button on:click={anonymousLogin}> Sign In Anonymously </button>
		</div>
	{/if}
</div>

<style>
	.kid {
	background-color: rgb(59, 93, 96);
	padding: 4rem;
	border-radius: 0; /* Remove border radius to make it square */
	box-shadow: 0 10px 20px rgba(0, 0, 0, 0.19), 0 6px 6px rgba(0, 0, 0, 0.23); /* Add box shadow for depth */
	width: 300px; /* Set a fixed width */
	height: 300px; /* Set a fixed height */
	display: flex;
	flex-direction: column;
	justify-content: space-between;
	}

	p {
		color: white;
		font-size: 0.9rem;
	}

	hr {
		border: 0;
		height: 1px;
		background-image: linear-gradient(to right, rgba(59, 93, 96, 0), rgba(59, 93, 96, 0.75), rgba(59, 93, 96, 0));
	}

	.center-text {
	text-align: center;
	}

	.google {
		margin-bottom: 0.25rem;
		background-color: rgb(59, 93, 96);
	}

	#parent {
		display: flex;
		justify-content: center;
		align-items: center;
		height: 100vh;
	}

	h1 {
		text-align: center;
		color: rgb(59, 93, 96);
		font-size: 2rem;
		margin-top: 50px; 
	}

	.signup-email {
		margin-top: 1rem;
		margin-bottom: 0.25rem;
	}

	input[type="text"], input[type="password"] {
		width: 100%;
		padding: 0.5rem;
		border: 1px solid #ddd;
		border-radius: 0.25rem;
	}

	button {
		width: 100%;
		padding: 0.75rem;
		border: none;
		border-radius: 0.25rem;
		color: #3b5d60;
		background-color: #fff;
		cursor: pointer;
		transition: box-shadow 0.3s ease, background-color 0.3s ease;
	}

	button:hover {
		box-shadow: 0 0 10px #3b5d60;
		background-color: #3b5d60;
		color: #fff;
	}
</style>
