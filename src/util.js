import { initializeApp } from "firebase/app";
import { getAuth} from 'firebase/auth';
import { GoogleAuthProvider } from 'firebase/auth';

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