import { writable } from 'svelte/store';

export const anonymousMode = writable(false);
export const authToken = writable('');
export const userData = writable({
	properties: [
		{
			name: 'Engineering and Computer Science West',
			picture: 'ecsw.jpg',
			address: '800 W. Campbell Road, Richardson, Texas',
			'sq-ft': 200000,
			value: 110000000,
			zipcode: '75080',
			assets: [
				{
					description: '',
					location: '',
					value: '',
					name: 'HVAC'
				}
			],
			'built-date': '01/04/2019',
			'defect-log': [
				{
					description: '',
					name: ''
				}
			],
			features: [
				{
					name: '',
					type: '',
					description: '',
					'maintenance-log': [
						{
							date: '',
							description: '',
							name: ''
						}
					]
				}
			],
			'property-notes': [
				{
					description: '',
					location: '',
					name: ''
				}
			],
			'renovation-log': [
				{
					cost: '',
					description: '',
					name: ''
				}
			],
			roof: {
				condition: 9,
				// 'replacement-date': '11/04/2080',
				'last-inspection': '2023-04-1',
				'warranty-expiration': '2026-11-15',
				type: 'metal'
			}
		},
		{
			name: 'Sample Property 1',
			picture: 'property1.jpg',
			address: '123 Main Street',
			'sq-ft': 5000,
			value: 1000000,
			zipcode: '12345',
			assets: [
				{
					description: 'HVAC System',
					location: 'Building A',
					value: '50000',
					name: 'AC Unit 1'
				},
				{
					description: 'Parking Lot',
					location: 'Parking Area',
					value: '20000',
					name: 'Parking Spaces'
				}
			],
			'built-date': '2000-05-15',
			'defect-log': [
				{
					description: 'Roof Leak',
					date: '2023-01-20',
					'repair-cost': '1500'
				},
				{
					description: 'Plumbing Issue',
					date: '2022-08-10',
					'repair-cost': '800'
				}
			],
			features: [
				{
					name: 'Security Cameras',
					type: 'Surveillance',
					description: '24/7 security monitoring'
				},
				{
					name: 'Conference Room',
					type: 'Meeting',
					description: 'Fully equipped conference room'
				}
			],
			'property-notes': [
				{
					date: '2023-02-15',
					note: 'Upcoming renovation planned'
				},
				{
					date: '2022-11-30',
					note: 'New tenant moved in'
				}
			],
			'renovation-log': [
				{
					description: 'Office Remodel',
					date: '2022-07-05',
					cost: '25000'
				},
				{
					description: 'Exterior Painting',
					date: '2021-03-10',
					cost: '10000'
				}
			],
			roof: {
				type: 'Flat Roof',
				condition: 'Good',
				'last-inspection': '2023-04-05',
				'warranty-expiration': '2025-12-31'
			}
		},
		{
			name: 'Sample Property 2',
			picture: 'property2.jpg',
			address: '456 Elm Street',
			'sq-ft': 8000,
			value: 1500000,
			zipcode: '54321',
			assets: [
				{
					description: 'Elevator',
					location: 'Building B',
					value: '35000',
					name: 'Elevator 1'
				}
			],
			'built-date': '1995-10-20',
			features: [],
			roof: {
				type: 'Pitched Roof',
				condition: 'Excellent',
				'last-inspection': '2023-03-15',
				'warranty-expiration': '2028-06-30'
			}
		},
		{
			name: 'Sample Property 3',
			picture: 'property3.jpg',
			address: '789 Oak Avenue',
			'sq-ft': 7000,
			value: 1200000,
			zipcode: '67890',
			assets: [
				{
					description: 'Retail Space',
					location: 'Building C',
					value: '40000',
					name: 'Storefront 1'
				},
				{
					description: 'Warehouse',
					location: 'Storage Area',
					value: '25000',
					name: 'Storage Space'
				}
			],
			'built-date': '2008-12-10',
			'defect-log': [
				{
					description: 'Electrical Issue',
					date: '2022-06-25',
					'repair-cost': '1200'
				}
			],
			features: [
				{
					name: 'High-Speed Internet',
					type: 'Technology',
					description: 'Fiber optic internet available'
				},
				{
					name: 'Cafeteria',
					type: 'Amenity',
					description: 'Employee dining area'
				}
			],
			'property-notes': [
				{
					date: '2023-03-20',
					note: 'Lease renewal in progress'
				},
				{
					date: '2022-10-15',
					note: 'New security system installed'
				}
			],
			'renovation-log': [
				{
					description: 'Interior Remodel',
					date: '2021-04-30',
					cost: '18000'
				},
				{
					description: 'Exterior Lighting Upgrade',
					date: '2020-09-12',
					cost: '7500'
				}
			],
			roof: {
				type: 'Flat Roof',
				condition: 'Good',
				'last-inspection': '2023-05-10',
				'warranty-expiration': '2026-11-15'
			}
		},
		{
			name: 'Sample Property 4',
			picture: 'property4.jpg',
			address: '101 Park Drive',
			'sq-ft': 6000,
			value: 1100000,
			zipcode: '54321',
			assets: [
				{
					description: 'Office Space',
					location: 'Building D',
					value: '60000',
					name: 'Office Suites'
				}
			],
			'built-date': '2010-08-15',
			features: [
				{
					name: 'Gym',
					type: 'Amenity',
					description: 'On-site fitness center'
				},
				{
					name: 'Lobby Art',
					type: 'Decor',
					description: 'Art installations in the lobby'
				}
			],
			'property-notes': [
				{
					date: '2023-01-25',
					note: 'New lease signed with XYZ Corporation'
				}
			],
			'renovation-log': [
				{
					description: 'HVAC System Upgrade',
					date: '2019-11-05',
					cost: '30000'
				}
			],
			roof: {
				type: 'Flat Roof',
				condition: 'Fair',
				'last-inspection': '2023-02-20',
				'warranty-expiration': '2027-09-30'
			}
		},
		{
			name: 'Sample Property 5',
			picture: 'property5.jpg',
			address: '222 Commerce Street',
			'sq-ft': 8500,
			value: 1400000,
			zipcode: '76543',
			assets: [
				{
					description: 'Restaurant Space',
					location: 'Building E',
					value: '55000',
					name: 'Kitchen Equipment'
				}
			],
			'built-date': '2005-04-22',
			'defect-log': [
				{
					description: 'Roof Leak',
					date: '2021-07-15',
					'repair-cost': '2000'
				}
			],
			features: [
				{
					name: 'Outdoor Patio',
					type: 'Amenity',
					description: 'Spacious outdoor dining area'
				},
				{
					name: 'Drive-Thru Window',
					type: 'Convenience',
					description: 'Drive-thru service available'
				}
			],
			'property-notes': [
				{
					date: '2023-04-05',
					note: 'New lease negotiations'
				},
				{
					date: '2022-09-10',
					note: 'Updated interior decor'
				}
			],
			'renovation-log': [
				{
					description: 'Kitchen Renovation',
					date: '2020-03-20',
					cost: '25000'
				},
				{
					description: 'Exterior Signage Upgrade',
					date: '2019-12-10',
					cost: '10000'
				}
			],
			roof: {
				type: 'Pitched Roof',
				condition: 'Good',
				'last-inspection': '2023-03-05',
				'warranty-expiration': '2026-10-20'
			}
		},
		{
			name: 'Sample Property 6',
			picture: 'property7.jpg',
			address: '456 Commercial Avenue',
			'sq-ft': 7500,
			value: 1300000,
			zipcode: '54321',
			assets: [
				{
					description: 'Office Space',
					location: 'Building G',
					value: '60000',
					name: 'Executive Suites'
				}
			],
			'built-date': '2012-03-18',
			features: [
				{
					name: 'Fitness Center',
					type: 'Amenity',
					description: 'On-site gym and workout facilities'
				},
				{
					name: 'Cafeteria',
					type: 'Amenity',
					description: 'Cafeteria with daily meal service'
				}
			],
			'property-notes': [
				{
					date: '2023-02-10',
					note: 'Lease negotiations with prospective tenant'
				},
				{
					date: '2022-09-22',
					note: 'Completed interior redesign'
				}
			],
			roof: {
				type: 'Flat Roof',
				condition: 'Good',
				'last-inspection': '2023-04-10',
				'warranty-expiration': '2027-10-30'
			}
		},
		{
			name: 'Sample Property 7',
			picture: 'property8.jpg',
			address: '789 Industrial Road',
			'sq-ft': 11000,
			value: 2000000,
			zipcode: '76543',
			assets: [
				{
					description: 'Manufacturing Equipment',
					location: 'Factory Building',
					value: '90000',
					name: 'Production Machines'
				}
			],
			'built-date': '2003-10-05',
			'defect-log': [
				{
					description: 'HVAC System Failure',
					date: '2021-12-18',
					'repair-cost': '3500'
				}
			],
			features: [
				{
					name: 'Industrial Ventilation',
					type: 'Safety',
					description: 'Air quality control systems'
				},
				{
					name: 'Loading Bays',
					type: 'Logistics',
					description: 'Multiple loading bays for shipping'
				}
			],
			'renovation-log': [
				{
					description: 'Factory Floor Expansion',
					date: '2020-08-30',
					cost: '25000'
				},
				{
					description: 'Office Space Renovation',
					date: '2019-05-12',
					cost: '12000'
				}
			],
			roof: {
				type: 'Pitched Roof',
				condition: 'Fair',
				'last-inspection': '2023-03-18',
				'warranty-expiration': '2028-09-15'
			}
		}
	]
});
