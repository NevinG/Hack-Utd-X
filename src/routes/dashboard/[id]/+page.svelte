<script>
	export let data;

	import { userData } from '../../../store';
	import { postData } from '../../../util.js';

	let assetDropdown = false;
	let featuresDropdown = false;
	let defectLogDropdown = false;
	let propertyNotesDropdown = false;
	let rennovationLogDropdown = false;
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
	<div>Size: <input bind:value={$userData.properties[data.id]['sq-ft']} /></div>
	<div>Built: <input bind:value={$userData.properties[data.id]['built-date']} /></div>
	<div>Value: $<input bind:value={$userData.properties[data.id]['value']} /></div>

	<div>
		<h1>
			Assets <button
				on:click={() => {
					assetDropdown = !assetDropdown;
				}}>+</button
			>
		</h1>
		{#if assetDropdown}
			{#each $userData.properties[data.id].assets as asset, i}
				<div style="display: flex; align-items: center">
					<button style="height: 50%">X</button>
					&nbsp;
					<div>
						<div>
							Name: <input
								placeholder="(name here)"
								bind:value={$userData.properties[data.id].assets[i]['name']}
							/>
						</div>
						<div>
							Value: $<input
								placeholder="(value here)"
								bind:value={$userData.properties[data.id].assets[i]['value']}
							/>
						</div>
						<div>
							Description: <input
								placeholder="(description here)"
								bind:value={$userData.properties[data.id].assets[i]['description']}
							/>
						</div>
					</div>
				</div>
				<br />
			{/each}
			<button
				on:click={() => {
					$userData.properties[data.id].assets.push({
						name: null,
						value: null,
						description: null
					});
					$userData = $userData;
				}}>Add New</button
			>
		{/if}
	</div>
	<div>
		<h1>
			Interior & Exterior <button
				on:click={() => {
					featuresDropdown = !featuresDropdown;
				}}>+</button
			>
		</h1>
		{#if featuresDropdown}
			{#each $userData.properties[data.id]['features'] as feature, i}
				<div style="display: flex; align-items: center">
					<button style="height: 50%">X</button>
					&nbsp;
					<div>
						<div>
							Name: <input
								placeholder="(name here)"
								bind:value={$userData.properties[data.id]['features'][i]['name']}
							/>
						</div>
						<div>
							Type: <input
								placeholder="(type here)"
								bind:value={$userData.properties[data.id]['features'][i]['type']}
							/>
						</div>
						<div>
							Description: <input
								placeholder="(description here)"
								bind:value={$userData.properties[data.id]['features'][i]['description']}
							/>
						</div>
						<br />
					</div>
				</div>
			{/each}
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
	<div>
		<h1>
			Defect Log <button
				on:click={() => {
					defectLogDropdown = !defectLogDropdown;
				}}>+</button
			>
		</h1>

		{#if defectLogDropdown}
			{#each $userData.properties[data.id]['defect-log'] as defectLog, i}
				<div style="display: flex; align-items: center">
					<button style="height: 50%">X</button>
					&nbsp;
					<div>
						<div>
							<input
								placeholder="(description here)"
								bind:value={$userData.properties[data.id]['defect-log'][i]['description']}
							/>
						</div>
						<div>
							<input
								placeholder="(date here)"
								bind:value={$userData.properties[data.id]['defect-log'][i]['date']}
							/>
						</div>
						<div>
							$<input
								placeholder="(repair cost here)"
								bind:value={$userData.properties[data.id]['defect-log'][i]['repair-cost']}
							/>
						</div>
						<br />
					</div>
				</div>
			{/each}
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
	<div>
		<h1>
			Property Notes <button
				on:click={() => {
					propertyNotesDropdown = !propertyNotesDropdown;
				}}>+</button
			>
		</h1>
		{#if propertyNotesDropdown}
			{#each $userData.properties[data.id]['property-notes'] as propertyNotes, i}
				<div style="display: flex; align-items: center">
					<button style="height: 50%">X</button>
					&nbsp;
					<div>
						<div>
							<input
								placeholder="(note here)"
								bind:value={$userData.properties[data.id]['property-notes'][i]['note']}
							/>
						</div>
						<div>
							<input
								placeholder="(date here)"
								bind:value={$userData.properties[data.id]['property-notes'][i]['date']}
							/>
						</div>
						<br />
					</div>
				</div>
			{/each}
			<button
				on:click={() => {
					$userData.properties[data.id]['property-notes'].push({
						note: null,
						date: null
					});
					$userData = $userData;
				}}>Add New</button
			>
		{/if}
	</div>
	<div>
		<h1>
			Rennovation Log <button
				on:click={() => {
					rennovationLogDropdown = !rennovationLogDropdown;
				}}>+</button
			>
		</h1>
		{#if rennovationLogDropdown}
			{#each $userData.properties[data.id]['renovation-log'] as renovationLog, i}
				<div style="display: flex; align-items: center">
					<button style="height: 50%">X</button>
					&nbsp;
					<div>
						<div>
							<input
								placeholder="(description)"
								bind:value={$userData.properties[data.id]['renovation-log'][i]['description']}
							/>
						</div>
						<div>
							<input
								placeholder="(date)"
								bind:value={$userData.properties[data.id]['renovation-log'][i]['date']}
							/>
						</div>
						<div>
							$<input
								placeholder="(cost)"
								bind:value={$userData.properties[data.id]['renovation-log'][i]['cost']}
							/>
						</div>
						<br />
					</div>
				</div>
			{/each}
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
		<h1>Narrative</h1>
		<p>condition report contents (to be filled)</p>
	</div>
	<button on:click={postData}>Save Data</button>
</div>

<style>
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
	#title-wrapper {
		display: flex;
		justify-content: center;
		flex-direction: column;
		align-items: center;
	}
</style>
