import { writable } from "svelte/store";

export const anonymousMode = writable(false);
export const authToken = writable('');
export const userData = writable({
    properties: [
      {
        name: "Engineering and Computer Science West",
        picture: "ecsw.jpg",
        address: "800 W. Campbell Road, Richardson, Texas",
        "sq-ft": 200000,
        value: 110000000,
        zipcode: "75080",
        assets: [
          {
            description: "",
            location: "",
            value: "",
            name: "HVAC",
          },
        ],
        "built-date": "01/04/2019",
        "defect-log": [
          {
            description: "",
            name: "",
          },
        ],
        features: [
          {
            name: "",
            type: "",
            description: "",
            "maintenance-log": [
              {
                date: "",
                description: "",
                name: "",
              },
            ],
          },
        ],
        "property-notes": [
          {
            description: "",
            location: "",
            name: "",
          },
        ],
        "renovation-log": [
          {
            cost: "",
            description: "",
            name: "",
          },
        ],
        roof: {
          condition: 9,
          "replacement-date": "11/04/2080",
          type: "metal",
        },
      }]
    });