import { initializeApp } from "firebase/app";
import { getAuth } from 'firebase/auth';
import { GoogleAuthProvider } from 'firebase/auth';
import { userData, authToken } from "./store.js";
import { get } from 'svelte/store'

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyCPOfHxcNpm3UBrIwq34dzaat804RYGsHM",
    authDomain: "hack-utd-x.firebaseapp.com",
    projectId: "hack-utd-x",
    storageBucket: "hack-utd-x.appspot.com",
    messagingSenderId: "332856366320",
    appId: "1:332856366320:web:c0e9f3fd2264fad9411e35",
    measurementId: "G-W0BZK0Y7GW"
};

// Initialize Firebase
export const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const provider = new GoogleAuthProvider();

export async function getData() {
    await fetchAuthToken();

    if(get(authToken) == ''){
        console.log('blank auth token')
        return;
    }
    try {
        let response = await fetch('http://10.122.130.26:3030/user', {
            headers: {
                'AuthToken': get(authToken),
                'Access-Control-Allow-Origin': 'no-cors'
            }   
        });
        const user = await response.json();
        if(user.exists){
            userData.set(user['user']);
        }
        console.log(user);
        return user;
    } catch (error) {
        console.log(error);
    }
}

export async function postData(){
    console.log("posting data");
    console.log("the data to post is:")
    console.log(get(userData))
    
    await fetchAuthToken();

    if(get(authToken) == ''){
        console.log('blank auth token')
        return;
    }
    try {
        let response = await fetch('http://10.122.130.26:3030/user', {
            method: 'PUT',
            headers: {
                'AuthToken': get(authToken),
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': 'no-cors'
            },
            body: JSON.stringify(get(userData))
        });
    } catch (error) {
        console.log(error);
    }
}

async function fetchAuthToken() {
    if (get(authToken) == '' && auth && auth.currentUser) {
        let response = await auth.currentUser.getIdToken(true);
        authToken.set(response);
    }
}