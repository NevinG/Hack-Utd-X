<script>
    import { auth, getData } from "../util.js";

    
    auth.onAuthStateChanged(function(user) {
        if (user != null) {
            getData();
        } else {
            console.log("error with user auth state change");
        }
    });
</script>

<slot />