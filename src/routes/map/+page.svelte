<script>
	import { Loader } from '@googlemaps/js-api-loader';
	import { onMount } from 'svelte';
	import { userData } from '../../store';
	import { PUBLIC_GOOGLE_MAPS_API_KEY } from '$env/static/public';

	import BackButton from '~icons/material-symbols/arrow-back';

	let map, mapDiv;
	let AdvancedMarkerElement, Geocoder;
	let geocodeCache = {};
	let markers = [];
	let properties = [];
	$: properties = $userData.properties;
	let selectedProperty;

	$: {
		if (map && AdvancedMarkerElement && Geocoder) {
			markers.forEach((m) => m.setMap(null));
			markers = getNewMarkers($userData.properties);
		}
	}

	async function getNewMarkers(properties) {
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

		loader.importLibrary('maps').then(({ Map }) => {
			navigator.geolocation.getCurrentPosition(async (position) => {
				const lat = position.coords.latitude;
				const lng = position.coords.longitude;

				map = new Map(mapDiv, {
					center: { lat, lng },
					zoom: 12,
					mapId: 'test'
				});
			});
		});

		loader.importLibrary('marker').then(({ AdvancedMarkerElement: m }) => {
			AdvancedMarkerElement = m;
		});

		loader.importLibrary('geocoding').then(({ Geocoder: g }) => {
			Geocoder = g;
		});
	});
</script>

<div class="container">
	<div class="header">
		<div class="back-button" on:click={() => window.history.back()} role="none"><BackButton /></div>
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
