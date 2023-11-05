<script>
	import { Loader } from '@googlemaps/js-api-loader';
	import { onMount } from 'svelte';
	import { userData } from '../../store';
	import { PUBLIC_GOOGLE_MAPS_API_KEY } from '$env/static/public';
	import { base } from '$app/paths';

	import BackButton from '~icons/material-symbols/arrow-back';

	let map, mapDiv;
	let AdvancedMarkerElement, Geocoder;
	let geocodeCache = {};
	let markers = [];
	let properties = [];
	$: properties = $userData.properties;
	let selectedProperty;
	$: if (!selectedProperty && properties) selectedProperty = properties[0].address;
	let requestedMarkers = false;

	userData.subscribe(({ properties }) => {
		if (!requestedMarkers && map && AdvancedMarkerElement && Geocoder) getNewMarkers(properties);
		if (properties && !properties.some((p) => p.address == selectedProperty))
			selectedProperty = properties[0].address;
	});

	async function getNewMarkers(properties) {
		requestedMarkers = true;

		markers.forEach((m) => m.setMap(null));

		const geocoder = new Geocoder();
		const newMarkers = [];
		for (const prop of properties) {
			const address = prop.address;
			if (!(address in geocodeCache)) {
				const { results } = await geocoder.geocode({ address });
				if (results.length === 0) geocodeCache[address] = null;
				else geocodeCache[address] = results[0];
			}
			const res = geocodeCache[address];
			if (!res) continue;
			newMarkers.push(
				new AdvancedMarkerElement({
					title: prop.name,
					position: res.geometry.location,
					map
				})
			);
		}
		markers = newMarkers;
		requestedMarkers = false;
	}

	function panToSelected() {
		const res = geocodeCache[selectedProperty];
		if (!res) return;
		map.panTo(res.geometry.location);
		map.setZoom(16);
	}

	onMount(() => {
		const loader = new Loader({
			apiKey: PUBLIC_GOOGLE_MAPS_API_KEY,
			version: 'weekly'
		});

		Promise.all([
			loader.importLibrary('maps').then(async ({ Map }) => {
				const coords = await new Promise((resolve) => {
					navigator.geolocation.getCurrentPosition(
						(position) => {
							const lat = position.coords.latitude;
							const lng = position.coords.longitude;
							resolve({ lat, lng });
						},
						() => {
							resolve({ lat: 32.985004100000005, lng: -96.7518982 });
						}
					);
				});
				map = new Map(mapDiv, {
					center: coords,
					zoom: 12,
					mapId: 'test'
				});
			}),
			loader.importLibrary('marker').then(({ AdvancedMarkerElement: m }) => {
				AdvancedMarkerElement = m;
			}),
			loader.importLibrary('geocoding').then(({ Geocoder: g }) => {
				Geocoder = g;
			})
		]).then(async () => {
			getNewMarkers($userData.properties);
		});
	});
</script>

<div class="container">
	<div class="header">
		<a class="back-button" href="{base}/dashboard"><BackButton /></a>
		<select id="property-select" bind:value={selectedProperty}>
			{#each properties as prop}
				<option value={prop.address}>{prop.name} ({prop.address})</option>
			{/each}
		</select>
		<button on:click={() => panToSelected()}>Go</button>
	</div>
	<div id="map" bind:this={mapDiv} />
</div>

<style lang="scss">
	:global(html),
	:global(body) {
		height: 100%;
		margin: 0;
		padding: 0;
	}

	.container {
		display: flex;
		flex-direction: column;
	}

	.header {
		height: 10vh;
		display: flex;
		flex-direction: row;
		align-items: center;
		gap: 0.25rem;

		padding-left: 1rem;
		padding-right: 1rem;

		font-size: 2rem;

		.back-button {
			cursor: pointer;
			display: flex;
			align-items: center;
		}

		select,
		button {
			height: 2rem;
		}
	}

	#map {
		height: 90vh;
		width: 100vw;
	}
</style>
