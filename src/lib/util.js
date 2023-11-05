export function formatValue(x) {
	let suffix = '';
	if (x > 1000000000) {
		x /= 1000000000;
		suffix += 'b';
	} else if (x > 1000000) {
		x /= 1000000;
		suffix += 'm';
	} else if (x > 1000) {
		x /= 1000;
		suffix += 'k';
	}
	x = Math.round(x * 10) / 10;
	return `${x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')}${suffix}`;
}

export function distanceBetweenLatLong(lat1, lon1, lat2, lon2) {
	// https://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula
	function deg2rad(deg) {
		return deg * (Math.PI / 180);
	}

	const R = 6371; // Radius of the earth in km
	const dLat = deg2rad(lat2 - lat1);
	const dLon = deg2rad(lon2 - lon1);
	const a =
		Math.sin(dLat / 2) * Math.sin(dLat / 2) +
		Math.cos(deg2rad(lat1)) * Math.cos(deg2rad(lat2)) * Math.sin(dLon / 2) * Math.sin(dLon / 2);
	const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
	const d = R * c; // Distance in km
	const m = d * 1000; // Distance in meters
	return m;
}
