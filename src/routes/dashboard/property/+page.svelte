<script>
	import { userData } from '../../../store';
	import {
		postData,
		getEnvironmentalReport,
		getPredictCondition,
		getPredictValueOverTime,
		getNarrative
	} from '../../../util.js';
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import { base } from '$app/paths';
	import LoadingIcon from '$lib/components/LoadingIcon.svelte';
	import Typewriter from 'svelte-typewriter';

	let assetDropdown = true;
	let featuresDropdown = true;
	let defectLogDropdown = true;
	let rennovationLogDropdown = true;

	let environmentalReportPromise = null;
	let narrativeReportPromise = null;
	let predictCondition = {};
	let predictValue = {};
	let loadingPredictCondition = true;
	let loadingPredictValue = true;
	let loadingEnvironmentalReport = true;
	let loadingNarrative = true;

	let id;

	onMount(async () => {
		id = $page.url.searchParams.get('id');
		if (!id) {
			alert('You need to call this route with a id query parameter');
		}

		predictCondition = await getPredictCondition($userData.properties[id]);
		console.log('predict condition: ');
		console.log(predictCondition);

		console.log('predict value: ');
		predictValue = await getPredictValueOverTime($userData.properties[id]);
		console.log(predictValue);

		environmentalReportPromise = getEnvironmentalReport($userData.properties[id]);
		// environmentalReport = environmentalReport['message'];

		narrativeReportPromise = getNarrative($userData.properties[id]);
		// narrative = narrative['message'];
	});
</script>

<!-- TODO IS TO get dat on back if it doesnt save -->
{#if id}
	<div id="title-wrapper">
		<div style="display: flex; justify-content: space-around; align-items: center;">
			<a href="{base}/dashboard">Back</a>
			<input
				placeholder="(name here)"
				class="input-title"
				bind:value={$userData.properties[id].name}
			/>
		</div>
		<div style="display: flex; flex-direction: row; ">
			<img src="/{$userData.properties[id].picture}" alt="commercial real estate property" />
			<div style="display: flex; flex-direction: column; justify-content: center;">
				<div class="bubble" style="display: flex; flex-direction: column; justify-content: center;">
					<div class="bubble-child">
						Size: <input
							placeholder="(sq-ft here)"
							bind:value={$userData.properties[id]['sq-ft']}
						/>
					</div>
					<div class="bubble-child">
						Built: <input
							placeholder="(build date here)"
							bind:value={$userData.properties[id]['built-date']}
						/>
					</div>
					<div class="bubble-child">
						Value: $<input
							placeholder="(value here)"
							bind:value={$userData.properties[id]['value']}
						/>
					</div>
					<div class="bubble-child">
						Address: $<input
							placeholder="(address here)"
							bind:value={$userData.properties[id]['address']}
						/>
					</div>
				</div>
			</div>
		</div>
		<div class="grid">
			<div class="container grid-item">
				<h1>
					Assets <button
						on:click={() => {
							assetDropdown = !assetDropdown;
						}}>+</button
					>
				</h1>
				{#if assetDropdown}
					<div class="dropdown">
						{#each $userData.properties[id].assets as asset, i}
							<div style="display: flex; align-items: center;">
								<div class="bubble">
									<div class="bubble-child">
										Name: <input
											placeholder="(name here)"
											bind:value={$userData.properties[id].assets[i]['name']}
										/>
									</div>
									<div class="bubble-child">
										Value: $<input
											placeholder="(value here)"
											bind:value={$userData.properties[id].assets[i]['value']}
										/>
									</div>
									<div class="bubble-child">
										Description: <input
											placeholder="(description here)"
											bind:value={$userData.properties[id].assets[i]['description']}
										/>
									</div>
									<div class="bubble-child">
										Latitude: <input
											placeholder="(lat here)"
											bind:value={$userData.properties[id].assets[i]['location']['lat']}
										/>
									</div>
									<div class="bubble-child">
										Longitude: <input
											placeholder="(long here)"
											bind:value={$userData.properties[id].assets[i]['location']['long']}
										/>
									</div>
								</div>
								<button
									style="height: 50%"
									on:click={() => {
										$userData.properties[id].assets.splice(i, 1);
										$userData = $userData;
									}}>X</button
								>
							</div>
						{/each}
					</div>
					<br />
					<button
						on:click={() => {
							$userData.properties[id].assets.push({
								name: '',
								value: '',
								description: '',
								location: {
									lat: '',
									long: ''
								}
							});
							$userData = $userData;
						}}>Add New</button
					>
				{/if}
			</div>
			<div class="container grid-item">
				<h1>
					Interior & Exterior <button
						on:click={() => {
							featuresDropdown = !featuresDropdown;
						}}>+</button
					>
				</h1>
				{#if featuresDropdown}
					{#each $userData.properties[id]['features'] as feature, i}
						<div style="display: flex; align-items: center;">
							<div class="bubble">
								<div class="bubble-child">
									Name: <input
										placeholder="(name here)"
										bind:value={$userData.properties[id]['features'][i]['name']}
									/>
								</div>
								<div class="bubble-child">
									Type: <input
										placeholder="(type here)"
										bind:value={$userData.properties[id]['features'][i]['type']}
									/>
								</div>
								<div class="bubble-child">
									Description: <input
										placeholder="(description here)"
										bind:value={$userData.properties[id]['features'][i]['description']}
									/>
								</div>
							</div>
							<button
								style="height: 50%"
								on:click={() => {
									$userData.properties[id]['features'].splice(i, 1);
									$userData = $userData;
								}}>X</button
							>
						</div>
					{/each}
					<br />
					<button
						on:click={() => {
							$userData.properties[id]['features'].push({
								name: '',
								type: '',
								description: ''
							});
							$userData = $userData;
						}}>Add New</button
					>
				{/if}
			</div>
			<div class="container grid-item">
				<h1>
					Defect Log <button
						on:click={() => {
							defectLogDropdown = !defectLogDropdown;
						}}>+</button
					>
				</h1>

				{#if defectLogDropdown}
					{#each $userData.properties[id]['defect-log'] as defectLog, i}
						<div style="display: flex; align-items: center;">
							<div class="bubble">
								<div class="bubble-child">
									<input
										placeholder="(description here)"
										bind:value={$userData.properties[id]['defect-log'][i]['description']}
									/>
								</div>
								<div class="bubble-child">
									<input
										placeholder="(date here)"
										bind:value={$userData.properties[id]['defect-log'][i]['date']}
									/>
								</div>
								<div class="bubble-child">
									$<input
										placeholder="(repair cost here)"
										bind:value={$userData.properties[id]['defect-log'][i]['repair-cost']}
									/>
								</div>
							</div>
							<button
								style="height: 50%"
								on:click={() => {
									$userData.properties[id]['defect-log'].splice(i, 1);
									$userData = $userData;
								}}>X</button
							>
						</div>
					{/each}
					<br />
					<button
						on:click={() => {
							$userData.properties[id]['defect-log'].push({
								description: '',
								date: '',
								'repair-cost': ''
							});
							$userData = $userData;
						}}>Add New</button
					>
				{/if}
			</div>
			<div class="container grid-item">
				<h1>
					Rennovation Log <button
						on:click={() => {
							rennovationLogDropdown = !rennovationLogDropdown;
						}}>+</button
					>
				</h1>
				{#if rennovationLogDropdown}
					{#each $userData.properties[id]['renovation-log'] as renovationLog, i}
						<div style="display: flex; align-items: center;">
							<div class="bubble">
								<div class="bubble-child">
									<input
										placeholder="(description)"
										bind:value={$userData.properties[id]['renovation-log'][i]['description']}
									/>
								</div>
								<div class="bubble-child">
									<input
										placeholder="(date)"
										bind:value={$userData.properties[id]['renovation-log'][i]['date']}
									/>
								</div>
								<div class="bubble-child">
									$<input
										placeholder="(cost)"
										bind:value={$userData.properties[id]['renovation-log'][i]['cost']}
									/>
								</div>
							</div>
							<button
								style="height: 50%"
								on:click={() => {
									$userData.properties[id]['renovation-log'].splice(i, 1);
									$userData = $userData;
								}}>X</button
							>
						</div>
					{/each}
					<br />
					<button
						on:click={() => {
							$userData.properties[id]['renovation-log'].push({
								description: '',
								date: '',
								cost: ''
							});
							$userData = $userData;
						}}>Add New</button
					>
				{/if}
			</div>
		</div>
		<div class="container">
			<!-- <h1>Condition Report</h1>
			<p>condition report contents (to be filled)</p> -->
			<h1>Environment</h1>
			<div class="report-container">
				{#if environmentalReportPromise}
					{#await environmentalReportPromise}
						<div class="loading"><LoadingIcon /></div>
					{:then data}
						<Typewriter><p>{data['message']}</p></Typewriter>
					{:catch error}
						<p>{error}</p>
					{/await}
				{/if}
			</div>
			<h1>Narrative</h1>
			<div class="report-container">
				{#if narrativeReportPromise}
					{#await narrativeReportPromise}
						<div class="loading"><LoadingIcon /></div>
					{:then data}
						<Typewriter><p>{data['message']}</p></Typewriter>
					{:catch error}
						<p>{error}</p>
					{/await}
				{/if}
			</div>
		</div>
		<button on:click={postData}>Save Data</button>
	</div>
{/if}

<style>
	@font-face {
		font-family: 'Montreal';
		src: url('/fonts/Montreal-Regular.woff') format('woff');
	}
	.container {
		display: flex;
		justify-content: center;
		align-items: center;
		flex-direction: column;
	}
	.grid-item {
	}
	.dropdown {
		overflow-y: scroll;
	}
	.report-container {
		padding: 20px;
		font-family: Montreal, serif;
		width: 80%;
	}
	.loading {
		display: flex;
		justify-content: center;
		align-items: center;
	}
	.grid {
		margin-top: 50px;
		width: 100vw;
		display: grid;
		grid-template-columns: 1fr 1fr;
		grid-template-rows: 1fr 1fr;
	}
	button {
		border-radius: 10px;
		background: transparent;
		margin: 5px;
		color: white;
		font-size: 30px;
	}
	button:hover {
		cursor: pointer;
	}
	h1 {
		display: flex;
		flex-direction: row;
	}
	.bubble {
		border-radius: 10px;
		padding: 10px 5px;
		margin: 5px;
		background-color: rgb(82, 129, 133);
		height: min-content;
	}
	.bubble-child {
		background-color: rgb(82, 129, 133);
	}
	img {
		max-width: 700px;
	}
	input {
		border: none;
		outline: none;
		/* border-bottom: 1px solid #ccc; You can adjust the color and thickness of the outline */
		/* background-color: rgb(90, 131, 134); */
		/* background-color: red; */
		background-color: transparent;
		color: white;
		font-family: Montreal, serif;
	}
	input:first-child {
		background-color: transparent;
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
	#title-wrapper {
		display: flex;
		justify-content: center;
		flex-direction: column;
		align-items: center;
		font-family: Montreal, serif;
	}
	img {
		border-radius: 20px;
	}
	.dropdown {
		overflow: hidden; /* Hide scrollbars */
	}
</style>
