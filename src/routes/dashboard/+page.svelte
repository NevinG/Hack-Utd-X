<script>
	import { signOut } from 'firebase/auth';
	import { auth, sampleProperty } from '../../util.js';
	import { userData, userExists } from '../../store.js';

	function logout() {
		signOut(auth);
		location.replace('/');
	}
</script>

{#if $userExists}
<div id="wrapper">
	<h1>Properties:</h1>
	{#each $userData['properties'] as property, i}
		<div>
			<a href="/dashboard/{i}"
				>{property.name ?? "New Property"}</a
			>
			<button on:click={() =>{
				$userData['properties'].splice(i,1);
				$userData = $userData;
				//TODO is to add push data
			}}>X</button>
		</div>
		<br/>
	{/each}
	<button on:click={()=>{
		$userData['properties'].push(sampleProperty);
		$userData = $userData;
	}}>Add property</button>
	<br/>
	<button on:click={logout}>logout</button>
</div>
{:else}
<p>Cant get data :(</p>
{/if}


<style>
	#wrapper{
		display: flex;
		justify-content: center;
		align-items: center;
		flex-direction: column;
	}
</style>
