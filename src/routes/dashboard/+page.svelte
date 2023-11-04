<script>
    import {signOut} from 'firebase/auth';
    import {auth} from '../../util.js';
    import { goto } from '$app/navigation';

    function logout(){
        signOut(auth);
        goto('/')
    }
</script>

<p>
    DASHBOARD
</p>

<button on:click={logout}>logout</button>