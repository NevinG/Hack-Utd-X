<script>
	import { currentAsset } from '$lib/stores/ar';

	export let asset;
</script>

<a-entity
	gps-new-entity-place="latitude: {asset.location.lat}; longitude: {asset.location.long}"
	look-at-id="camera"
	material="opacity: 0.75; color: #FFFFFF"
	geometry="primitive: circle"
	on:click|capture|stopPropagation={() => currentAsset.set(asset)}
	role="none"
	scale="0.5 0.5 1"
	position="0 1 0"
>
	<a-entity
		text__name="align: center; baseline: bottom; value: {asset.name}; width: 10"
		position="0 0.1 0.1"
	/>
</a-entity>
