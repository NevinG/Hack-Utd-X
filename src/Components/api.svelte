<script>
    import { userData } from "../store";
    import { auth } from "../util.js";

    let authToken = '';

    export async function getData() {
        await fetchAuthToken();

        if(authToken == ''){
            console.log('blank auth token')
            return;
        }
        try {
            let response = await fetch('http://10.122.130.26:3030/user', {
                headers: {
                    'AuthToken': authToken,
                    'Access-Control-Allow-Origin': 'no-cors'
                }   
            });
            const user = await response.json();
            if(user.exists){
                $userData = user['user'];
            }
            console.log(user);
        } catch (error) {
            console.log(error);
        }
    }

    async function fetchAuthToken() {
        if (auth && auth.currentUser) {
            authToken = await auth.currentUser.getIdToken(true);
        }
    }
</script>