<script>
    import {signOut} from 'firebase/auth';
    import {auth} from '../../util.js';
    import { goto } from '$app/navigation';
    import { userData } from '../../store.js';

    function logout(){
        signOut(auth);
        goto('/')
    }
</script>

<h1>properties:</h1>
{#each $userData["properties"] as property}
    <div>   
        <p>{property.name}</p>
    </div>
{/each}

<button on:click={logout}>logout</button>