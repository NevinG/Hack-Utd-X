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

<style>
    :global(div){
        background-color: rgb(1,42,45);
    }
    :global(h1){
		color: white;
	}
	:global(a){
		color: white;
		text-decoration: none;
	}
	:global(a:hover){
		color: white;
		text-decoration: underline;
	}
    :global(p){
		color: white;
	}
    :global(div){
		color: white;
	}
    :global(::placeholder) {
        color: rgb(200,200,200);
        opacity: 1; /* Firefox */
    }

</style>