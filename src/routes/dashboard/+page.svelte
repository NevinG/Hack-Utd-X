<script>
	import { signOut } from 'firebase/auth';
	import { auth, sampleProperty } from '../../util.js';
	import { userData, userExists } from '../../store.js';
	import { base } from '$app/paths';
	import { page } from '$app/stores';

	function logout() {
		signOut(auth);
		location.replace('/');
	}
</script>

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
	<p>Cant get data :(</p>
{/if}

<style>
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
	}
	.property-parent {
		display: flex;
	}
	.button-container {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}
</style>
