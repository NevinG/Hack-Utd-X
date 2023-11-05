<script>
	export let data;

	import { userData } from '../../../store';
	import { postData, getEnvironmentalReport, getPredictCondition, getPredictValueOverTimer, getNarrative } from '../../../util.js';
	import { onMount } from 'svelte';

	let assetDropdown = false;
	let featuresDropdown = false;
	let defectLogDropdown = false;
	let rennovationLogDropdown = false;

	let environmentalReport = "";
	let narrative = "";

	for(let i = 0; i < $userData.properties[data.id].assets.length; i++){
		$userData.properties[data.id].assets[i]['location'] = {
			"lat": "",
			"long": "",
		}
	}

	onMount(async () => {
		environmentalReport = await getEnvironmentalReport($userData.properties[data.id])['message'];
		narrative = await getNarrative($userData.properties[data.id])['message'];
		//environmentalReport = await getEnvironmentalReport()['message'];
		//environmentalReport = await getEnvironmentalReport()['message'];
	});
</script>

<!-- TODO IS TO get dat on back if it doesnt save -->
<a href="/dashboard">Back</a>
<div id="title-wrapper">
	<div>
		<input
			placeholder="(name here)"
			class="input-title"
			bind:value={$userData.properties[data.id].name}
		/>
	</div>
	<img src="/{$userData.properties[data.id].picture}" alt="commercial real estate property" />
	<br>
	<div class="bubble">
	<div class="bubble-child">Size: <input placeholder="(sq-ft here)" bind:value={$userData.properties[data.id]['sq-ft']} /></div>
	<div class="bubble-child">Built: <input placeholder="(build date here)" bind:value={$userData.properties[data.id]['built-date']} /></div>
	<div class="bubble-child">Value: $<input placeholder="(value here)" bind:value={$userData.properties[data.id]['value']} /></div>
	<div class="bubble-child">Address: $<input placeholder="(address here)" bind:value={$userData.properties[data.id]['address']} /></div>
	</div>

	<div class="container">
		<h1>
			Assets <button
				on:click={() => {
					assetDropdown = !assetDropdown;
				}}>+</button
			>
		</h1>
		{#if assetDropdown}
			{#each $userData.properties[data.id].assets as asset, i}
				<div style="display: flex; align-items: center;">
					<div class="bubble">
						<div class = "bubble-child">
							Name: <input
								placeholder="(name here)"
								bind:value={$userData.properties[data.id].assets[i]['name']}
							/>
						</div>
						<div class = "bubble-child">
							Value: $<input
								placeholder="(value here)"
								bind:value={$userData.properties[data.id].assets[i]['value']}
							/>
						</div>
						<div class = "bubble-child">
							Description: <input
								placeholder="(description here)"
								bind:value={$userData.properties[data.id].assets[i]['description']}
							/>
						</div>
						<div class = "bubble-child">
							Latitude: <input
								placeholder="(lat here)"
								bind:value={$userData.properties[data.id].assets[i]['location']['lat']}
							/>
						</div>
						<div class = "bubble-child">
							Longitude: <input
								placeholder="(long here)"
								bind:value={$userData.properties[data.id].assets[i]['location']['long']}
							/>
						</div>
					</div>
					<button style="height: 50%" on:click={() => {$userData.properties[data.id].assets.splice(i,1); $userData=$userData}}>X</button>
				</div>
			{/each}
			<br/>
			<button
				on:click={() => {
					$userData.properties[data.id].assets.push({
						name: null,
						value: null,
						description: null,
						location: {
							lat: null,
							long: null
						}
					});
					$userData = $userData;
				}}>Add New</button
			>
		{/if}
	</div>
	<div class="container">
		<h1>
			Interior & Exterior <button
				on:click={() => {
					featuresDropdown = !featuresDropdown;
				}}>+</button
			>
		</h1>
		{#if featuresDropdown}
			{#each $userData.properties[data.id]['features'] as feature, i}
				<div style="display: flex; align-items: center;">
					<div class="bubble">
						<div class = "bubble-child">
							Name: <input
								placeholder="(name here)"
								bind:value={$userData.properties[data.id]['features'][i]['name']}
							/>
						</div>
						<div class = "bubble-child">
							Type: <input
								placeholder="(type here)"
								bind:value={$userData.properties[data.id]['features'][i]['type']}
							/>
						</div>
						<div class = "bubble-child">
							Description: <input
								placeholder="(description here)"
								bind:value={$userData.properties[data.id]['features'][i]['description']}
							/>
						</div>
					</div>
					<button style="height: 50%" on:click={() => {$userData.properties[data.id]['features'].splice(i,1); $userData=$userData}}>X</button>
				</div>
			{/each}
			<br/>
			<button
				on:click={() => {
					$userData.properties[data.id]['features'].push({
						name: null,
						type: null,
						description: null
					});
					$userData = $userData;
				}}>Add New</button
			>
		{/if}
	</div>
	<div class="container">
		<h1>
			Defect Log <button
				on:click={() => {
					defectLogDropdown = !defectLogDropdown;
				}}>+</button
			>
		</h1>

		{#if defectLogDropdown}
			{#each $userData.properties[data.id]['defect-log'] as defectLog, i}
				<div style="display: flex; align-items: center;">
					<div class="bubble">
						<div class = "bubble-child">
							<input
								placeholder="(description here)"
								bind:value={$userData.properties[data.id]['defect-log'][i]['description']}
							/>
						</div>
						<div class = "bubble-child">
							<input
								placeholder="(date here)"
								bind:value={$userData.properties[data.id]['defect-log'][i]['date']}
							/>
						</div>
						<div class = "bubble-child">
							$<input
								placeholder="(repair cost here)"
								bind:value={$userData.properties[data.id]['defect-log'][i]['repair-cost']}
							/>
						</div>
					</div>
					<button style="height: 50%" on:click={() => {$userData.properties[data.id]['defect-log'].splice(i,1); $userData=$userData}}>X</button>
				</div>
			{/each}
			<br/>
			<button
				on:click={() => {
					$userData.properties[data.id]['defect-log'].push({
						description: null,
						date: null,
						'repair-cost': null
					});
					$userData = $userData;
				}}>Add New</button
			>
		{/if}
	</div>
	<div class="container">
		<h1>
			Rennovation Log <button
				on:click={() => {
					rennovationLogDropdown = !rennovationLogDropdown;
				}}>+</button
			>
		</h1>
		{#if rennovationLogDropdown}
			{#each $userData.properties[data.id]['renovation-log'] as renovationLog, i}
				<div style="display: flex; align-items: center;">
					<div class="bubble">
						<div class = "bubble-child">
							<input
								placeholder="(description)"
								bind:value={$userData.properties[data.id]['renovation-log'][i]['description']}
							/>
						</div>
						<div class = "bubble-child">
							<input
								placeholder="(date)"
								bind:value={$userData.properties[data.id]['renovation-log'][i]['date']}
							/>
						</div>
						<div class = "bubble-child">
							$<input
								placeholder="(cost)"
								bind:value={$userData.properties[data.id]['renovation-log'][i]['cost']}
							/>
						</div>
					</div>
					<button style="height: 50%" on:click={() => {$userData.properties[data.id]['renovation-log'].splice(i,1); $userData=$userData}}>X</button>
				</div>
			{/each}
			<br/>
			<button
				on:click={() => {
					$userData.properties[data.id]['renovation-log'].push({
						description: null,
						date: null,
						cost: null
					});
					$userData = $userData;
				}}>Add New</button
			>
		{/if}
	</div>
	<div>
		<h1>Condition Report</h1>
		<p>condition report contents (to be filled)</p>
		<h1>Enviornment Report</h1>
		<p>{environmentalReport}</p>
		<h1>Narrative</h1>
		<p>{narrative}</p>
	</div>
	<button on:click={postData}>Save Data</button>
</div>

<style>
	.container{
		display: flex;
		justify-content: center;
		align-items: center;
		flex-direction: column;
	}
	.bubble{
		border-radius: 10px;
		padding: 25px;
		margin: 5px;
		background-color: rgb(82,129,133);
	}
	.bubble-child{
		background-color: rgb(82,129,133);
	}
	img {
		max-width: 100%;
	}
	input {
		border: none;
		outline: none;
		/* border-bottom: 1px solid #ccc; You can adjust the color and thickness of the outline */
		background-color: none;
	}
	.input-title {
		display: block;
		font-size: 2em;
		margin-top: 0.67em;
		margin-bottom: 0.67em;
		margin-left: 0;
		margin-right: 0;
		font-weight: bold;
		text-align: center;
	}
	input{
		background-color: transparent;
		color: white;
	}
	#title-wrapper {
		display: flex;
		justify-content: center;
		flex-direction: column;
		align-items: center;
	}
	img{
		border-radius: 20px;
	}
</style>
