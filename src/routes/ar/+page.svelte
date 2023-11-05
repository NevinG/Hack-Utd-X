<script>
	import { onMount } from 'svelte';
	import ArAsset from '$lib/components/ArAsset.svelte';
	import LoadingIcon from '$lib/components/LoadingIcon.svelte';
	import { currentAsset } from '$lib/stores/ar';
	import { fly } from 'svelte/transition';
	import { userData } from '../../store';
	import { formatValue, distanceBetweenLatLong } from '$lib/util.js';
	import { page } from '$app/stores';

	import HomeIcon from '~icons/material-symbols/home';
	import CloseIcon from '~icons/carbon/close';

	import ArThreeUrl from '@ar-js-org/ar.js/three.js/build/ar-threex-location-only?url';
	import ArAFrameUrl from '@ar-js-org/ar.js/aframe/build/aframe-ar?url';
	import ArAddonsUrl from '$lib/scripts/araddons.js?url';
	const AFrameUrl = 'https://aframe.io/releases/1.4.0/aframe.min.js';
	const externalLibraryCount = 4;

	let loadCount = 0;
	let assets = null;
	let mounted = false;
	let ready = false;
	$: ready = loadCount === externalLibraryCount && mounted && assets != null;

	let lat = null;
	let long = null;
	let propertyNames = $userData.properties.map((p) => p.name);
	let floors = [0];
	$: floors = Array.from(new Set((assets ?? [{ floor: 0 }]).map((a) => a.floor ?? 0))).sort();
	let selectedFloor = 0;
	let selectedProperty = $userData.properties[0].name;
	$: {
		if (selectedProperty) {
			const property = $userData.properties.find((p) => p.name === selectedProperty);
			if (property) {
				let tempAssets = property.assets;
				tempAssets.forEach((a) => {
					if (!('floor' in a)) a.floor = 0;
				});
				tempAssets = property.assets.filter((a) => {
					return typeof a.location !== 'string' && 'lat' in a.location && 'long' in a.location;
				});
				assets = tempAssets;
			}
		}
	}

	function onLibraryLoad() {
		loadCount++;
		console.log('load count:', loadCount);
	}

	function resetPosition() {
		navigator.geolocation.getCurrentPosition(async (position) => {
			lat = position.coords.latitude;
			long = position.coords.longitude;
			console.log('lat:', lat);
			console.log('long:', long);
		});
	}

	onMount(() => {
		loadCount = 0;
		mounted = true;
		resetPosition();
		if (
			$page.url.searchParams.has('property') &&
			propertyNames.includes($page.url.searchParams.get('property'))
		) {
			selectedProperty = $page.url.searchParams.get('property');
		}
	});
</script>

<svelte:head>
	<link
		href="https://fonts.googleapis.com/css?family=Roboto:regular,black&display=swap"
		rel="stylesheet"
	/>
	<title>Asset Visualizer</title>
	{#if mounted}
		<script src={AFrameUrl} on:load={onLibraryLoad}></script>
		{#if loadCount >= 1}
			<script type="text/javascript" src={ArThreeUrl} on:load={onLibraryLoad}></script>
			<script type="text/javascript" src={ArAFrameUrl} on:load={onLibraryLoad}></script>
			<script type="text/javascript" src={ArAddonsUrl} on:load={onLibraryLoad}></script>
		{/if}
	{/if}
</svelte:head>

{#if ready}
	<a-scene
		vr-mode-ui="enabled: false"
		arjs="sourceType: webcam; videoTexture: true; debugUIEnabled: false"
		renderer="antialias: true; alpha: true"
	>
		<a-camera
			id="camera"
			gps-new-camera="gpsMinDistance: 5;"
			on:gps-camera-update-position={(data) => {
				const pos = data.detail.position;
				lat = pos.latitude;
				long = pos.longitude;
				console.log('GPS update:', lat, long);
			}}
			arjs-device-orientation-controls="smoothingFactor: 0.1"
			cursor="rayOrigin: mouse"
		>
			<a-entity
				cursor="fuse: true; fuseTimeout: 1"
				position="0 0 -1"
				geometry="primitive: ring; radiusInner: 0.02; radiusOuter: 0.03"
				material="color: white; shader: flat"
			/>
		</a-camera>
		{#if assets !== null}
			{#each assets.filter((a) => a.floor === selectedFloor) as asset}
				<ArAsset {asset} />
			{/each}
		{/if}
	</a-scene>
	<div id="ar-overlay">
		<div class="header">
			<a href="/">
				<HomeIcon />
			</a>
			<select id="property-select" bind:value={selectedProperty}>
				{#each propertyNames as name}
					<option value={name}>{name}</option>
				{/each}
			</select>
			<select id="floor-select" bind:value={selectedFloor}>
				{#each floors as floor}
					<option value={floor}>{floor}</option>
				{/each}
			</select>
		</div>
		{#if $currentAsset !== null}
			<div
				class="footer"
				transition:fly={{
					duration: 300,
					y: 500
				}}
			>
				<div class="close" on:click={() => ($currentAsset = null)} role="none">
					<CloseIcon />
				</div>
				<div class="body">
					<h2><b>{$currentAsset.name}</b></h2>
					<h2>{$currentAsset.description}</h2>
					<h2>${formatValue($currentAsset.value ?? 0)}</h2>
					<br />
					<h2>
						{Math.round(
							distanceBetweenLatLong(
								lat,
								long,
								$currentAsset.location.lat,
								$currentAsset.location.long
							) * 100
						) / 100} meters away
					</h2>
					<span class="spacer" />
				</div>
			</div>
		{/if}
	</div>
{:else}
	<LoadingIcon />
{/if}

<style lang="scss">
	#ar-overlay {
		position: absolute;
		left: 0;
		top: 0;

		width: 100vw;
		height: 100vh;

		color: white;

		font-family: 'Roboto', sans-serif;

		b,
		a {
			font-weight: 900;
		}

		h2 {
			font-weight: 400;
		}

		a {
			font-size: 1.75em;
			color: white;
		}

		.header {
			padding: 1em;
			display: flex;
			flex-direction: row;
			align-items: center;
			gap: 1em;
			width: 100%;
		}

		.footer {
			position: absolute;
			top: 60vh;
			left: 0;
			width: 100%;

			padding: 1em;
			background-color: rgba(0, 0, 0, 0.5);

			.close {
				position: absolute;
				right: 3em;
				top: 1em;
			}

			.body {
				overflow-y: auto;
				height: 40vh;
			}

			.spacer {
				display: block;
				width: 100%;
				height: 10vh;
			}
		}
	}
</style>
