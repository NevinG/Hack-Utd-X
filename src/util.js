import { initializeApp } from 'firebase/app';
import { getAuth } from 'firebase/auth';
import { GoogleAuthProvider } from 'firebase/auth';
import { userData, authToken, anonymousMode, userExists } from './store.js';
import { get } from 'svelte/store';

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
	apiKey: 'AIzaSyCPOfHxcNpm3UBrIwq34dzaat804RYGsHM',
	authDomain: 'hack-utd-x.firebaseapp.com',
	projectId: 'hack-utd-x',
	storageBucket: 'hack-utd-x.appspot.com',
	messagingSenderId: '332856366320',
	appId: '1:332856366320:web:c0e9f3fd2264fad9411e35',
	measurementId: 'G-W0BZK0Y7GW'
};

// Initialize Firebase
export let app = initializeApp(firebaseConfig);
export let auth = getAuth(app);
export let provider = new GoogleAuthProvider();

export const sampleProperty = {
	name: null,
	picture: 'ecsw.jpg',
	address: null,
	'sq-ft': null,
	value: null,
	zipcode: null,
	assets: [
		{
			description: null,
			location: {
				lat: null,
				long: null,
			},
			value: null,
			name: null
		}
	],
	'built-date': null,
	'defect-log': [
		{
			description: null,
			name: null
		}
	],
	features: [
		{
			name: null,
			type: null,
			description: null,
			'maintenance-log': [
				{
					date: null,
					description: null,
					name: null
				}
			]
		}
	],
	'property-notes': [
		{
			description: null,
			location: null,
			name: null
		}
	],
	'renovation-log': [
		{
			cost: null,
			description: null,
			name: null
		}
	],
	roof: {
		condition: null,
		'replacement-date': null,
		type: null
	}
};

export async function getData(n = 0) {
	await fetchAuthToken();

	if (get(authToken) == '') {
		console.log('blank auth token');
		return;
	}
	try {
		let response = await fetch('http://localhost:3030/user', {
			headers: {
				AuthToken: get(authToken),
				'Access-Control-Allow-Origin': 'no-cors'
			}
		});
		const user = await response.json();
		userExists.set(user.exists);
		if (user.exists) {
			userData.set(user['user']);
		} else {
			userData.set(user['user']);
		}
	} catch (error) {
		console.log(n);
		if (n != 1) {
			if (n == 0) n = 5;
			n--;
			setTimeout(() => {
				getData(n);
			}, 200);
		}
		console.log(error);
	}
}

export async function postData() {
	if (get(anonymousMode)) {
		console.log('YORUE IN ANONYNOUS MODE, YOU CANNOT POST DATA');
		return;
	}

	await fetchAuthToken();

	if (get(authToken) == '') {
		console.log('blank auth token');
		return;
	}
	try {
		let response = await fetch('http://localhost:3030/user', {
			method: 'POST',
			headers: {
				AuthToken: get(authToken),
				'Content-Type': 'application/json',
				'Access-Control-Allow-Origin': 'no-cors'
			},
			body: JSON.stringify(get(userData))
		});
	} catch (error) {
		console.log(error);
	}
}

export async function getEnvironmentalReport(propertyData) {
	await fetchAuthToken();
	if (get(authToken) == '') {
		console.log('blank auth token');
		return;
	}
	try {
		let response = await fetch('http://localhost:3030/get_environmental_report', {
			method: 'POST',
			headers: {
				AuthToken: get(authToken),
				'Content-Type': 'application/json',
				'Access-Control-Allow-Origin': 'no-cors'
			},
			body: JSON.stringify(propertyData)
		});
		const data = await response.json();
		return data;
	} catch (error) {
		console.log(error);
	}
}

export async function getNarrative(propertyData) {
	await fetchAuthToken();
	if (get(authToken) == '') {
		console.log('blank auth token');
		return;
	}
	try {
		let response = await fetch('http://localhost:3030/get_narrative', {
			method: 'POST',
			headers: {
				AuthToken: get(authToken),
				'Content-Type': 'application/json',
				'Access-Control-Allow-Origin': 'no-cors'
			},
			body: JSON.stringify(propertyData)
		});
		const data = await response.json();
		return data;
	} catch (error) {
		console.log(error);
	}
}

export async function getPredictValueOverTime(propertyData) {
	await fetchAuthToken();
	if (get(authToken) == '') {
		console.log('blank auth token');
		return;
	}
	try {
		let response = await fetch('http://localhost:3030/get_predict_value_over_time', {
			method: 'POST',
			headers: {
				AuthToken: get(authToken),
				'Content-Type': 'application/json',
				'Access-Control-Allow-Origin': 'no-cors'
			},
			body: JSON.stringify(propertyData)
		});
		const data = await response.json();
		return data;
	} catch (error) {
		console.log(error);
	}
}

export async function getPredictCondition(propertyData) {
	await fetchAuthToken();
	if (get(authToken) == '') {
		console.log('blank auth token');
		return;
	}
	try {
		let response = await fetch('http://localhost:3030/get_predict_condition', {
			method: 'POST',
			headers: {
				AuthToken: get(authToken),
				'Content-Type': 'application/json',
				'Access-Control-Allow-Origin': 'no-cors'
			},
			body: JSON.stringify(propertyData)
		});
		const data = await response.json();
		return data;
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
