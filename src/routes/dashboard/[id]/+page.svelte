<script>
	// /** @type {import('./$types').PageData} */
	import '../../../app.postcss';
	export let data;

	import { userData } from '../../../store';

	const property = $userData.properties[data.id];
	const USDollar = new Intl.NumberFormat('en-US', {
		style: 'currency',
		currency: 'USD'
	});

	// const interiorFeatures = property.features.filter((feature) => feature.type == 'interior');
</script>

<h1>{data.id}</h1>

<div class="w-screen h-screen flex flex-col p-10 items-center">
	<div class="rounded-md bg-slate-300 py-3 px-5">
		<h1 class="text-xl font-bold">{property.name}</h1>
		<div>Size: {property['sq-ft']}</div>
		<div>Built: {property['built-date']}</div>
		<div>
			{USDollar.format(property.value)}
		</div>

		<img src="/{property.picture}" alt="commercial real estate property" />
	</div>
	<div class="grid grid-cols-3 grid-rows-3 gap-4 w-4/5">
		<div>
			<h1 class="text-xl font-bold">Assets</h1>
			<ul>
				{#each property.assets as asset}
					<li>{asset.name}, {USDollar.format(asset.value)}</li>
					<li>{asset.description}</li>
				{/each}
			</ul>
		</div>
		<div>
			<h1 class="text-xl font-bold">Interior & Exterior</h1>
			{#each property['features'] as feature}
				<li>{feature.name}, {feature.type}</li>
				<li>{feature.description}</li>
			{/each}
		</div>
		<div>
			<h1 class="text-xl font-bold">Defect Log</h1>
			<ul>
				{#each property['defect-log'] as defectLog}
					<li>{defectLog.description}, {defectLog.date}</li>
					<li>
						{USDollar.format(defectLog['repair-cost']) !== NaN
							? USDollar.format(defectLog['repair-cost'])
							: ''}
					</li>
				{/each}
			</ul>
		</div>
		<div>
			<h1 class="text-xl font-bold">Property Notes</h1>
			<ul>
				{#each property['property-notes'] as propertyNotes}
					<li>{propertyNotes.note}, {propertyNotes.date}</li>
				{/each}
			</ul>
		</div>
		<div>
			<h1 class="text-xl font-bold">Renovation Log</h1>
			<ul>
				{#each property['renovation-log'] as renovationLog}
					<li>{renovationLog.description}, {renovationLog.date}</li>
					<li>
						{USDollar.format(renovationLog['cost']) !== NaN
							? USDollar.format(renovationLog['cost'])
							: ''}
					</li>
				{/each}
			</ul>
		</div>
		<div>
			<h1>Condition Report</h1>
			<h1>Narrative</h1>
		</div>
	</div>
</div>

<style>
	img {
		max-width: 100%;
	}
</style>
