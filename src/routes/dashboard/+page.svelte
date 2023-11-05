<script>
	import { signOut } from 'firebase/auth';
	import { auth, sampleProperty } from '../../util.js';
	import { userData, userExists } from '../../store.js';
	import LoadingIcon from '$lib/components/LoadingIcon.svelte';
	import { base } from '$app/paths';
	import { page } from '$app/stores';

	import MapIcon from '~icons/material-symbols/location-on';
	import CameraIcon from '~icons/material-symbols/camera';

	function logout() {
		signOut(auth);
		location.replace('/');
	}
</script>

<div id="overlay">
	<a href="{base}/map"><MapIcon /></a>
	<a href="{base}/ar"><CameraIcon /></a>
</div>

{#if $userExists}
	<div id="wrapper">
		<h1>Properties:</h1>
		{#each $userData['properties'] as property, i}
			<div class="property-parent">
				<div class="property">
					<a href="{base}/dashboard/property?id={i}">{property.name ?? 'New Property'}</a>
					<br />
				</div>
				<div class="button-container">
					<button
						on:click={() => {
							$userData['properties'].splice(i, 1);
							$userData = $userData;
							//TODO is to add push data
						}}>X</button
					>
				</div>
			</div>
		{/each}
		<button
			on:click={() => {
				$userData['properties'].push(sampleProperty);
				$userData = $userData;
			}}>Add property</button
		>
		<br />
		<button on:click={logout}>logout</button>
	</div>
{:else}
	<div id="loading-container">
		<LoadingIcon />
	</div>
{/if}

<style>
	#loading-container {
		width: 100%;
		height: 100%;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	#overlay {
		position: absolute;
		left: 1rem;
		top: 1rem;
		height: 2rem;
		font-size: 2rem;
	}

	#wrapper {
		display: flex;
		justify-content: center;
		align-items: center;
		flex-direction: column;
	}
	.property {
		border-radius: 10px;
		padding: 25px;
		margin: 5px;
		background-color: rgb(82, 129, 133);
		width: 100%;
	}
	.property-parent {
		display: flex;
		width: 100%;
		max-width: 400px;
	}
	.button-container {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}
</style>
