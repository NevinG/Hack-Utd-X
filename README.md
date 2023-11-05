# Property Prober

[propertyprober.co](https://www.propertyprober.co/)

## How we used GitHub

During development, we used three key GitHub features:

- [Actions & Pages](#actions)
- [Issues & Pull Requests](#issues--pull-requests)
- [Projects](#projects)

#### Actions

We used actions to automatically build the SvelteKit website and update GitHub Pages whenever we committed to main. This allowed us to instantly test our changes in production and to save time by not manually building. Futhermore, since GitHub pages supports custom domains, were are able to use it for a full deployment.

![Screenshot of GitHub actions page](./static/gh_actions.png)

#### Issues & Pull Requests

We used issues to keep track of what we are working on and what we need to do. This made sure we don't forget to fix bugs or other issues as we are working. Issues also allowed us to assign tasks to other team members to help spread the workload. Pull requests also made sure that we did not commit changes to main that cause merge conflicts. Pull requests also allowed for large changes to be tracked and assigned to issues.

![Screenshot of GitHub Issues/PR page](./static/gh_issues.png)

#### Projects

Alongside issues and pull requests, we used a GitHub project to keep track of the overall progress of the project. At the beginning of the project, we added all of the tasks that we needed to get done. As we worked through them, we updated each task's status to in progress and then done. We also kept track of new tasks as they came up and assigned them to team members using projects.

![Screenshot of GitHub Projects Page](./static/gh_projects.png)

## Our Inspiration

We were inspired by the CBRE challenge to develop a solution to manage and asses properties and their conditions. We were also inspired to focus on how this project will be used in the real world. Different stakeholders have different requirements, so we built our webapp to provide unique features to each of these users.

Managers can use high-level functions for viewing properties from a local to nation-wide scale using AI technology. Technicians and property owners have innovative tools to view and generate new assets using augmented reality. Focussing on these different user groups while developing an innovative app was our primary motivation.

## What it does

We are a one-stop-shop for all of your commercial real estate needs.

The core of our project is a list of tracked properties. Each of these properties are fully editable and synced with a secure database. AI provides a high-level environmental report and narrative description of the property's current and predicted condition. Finally, an augmented reality tool allows users to find assets stored in the database in the real world, and it allows a room to scanned for new assets. The value of these assets are calculated using online sources, and their total is given to provide the user.

## How we built it

Along with blood, sweat, and tears, we built the project with various technologies. We used HTML, CSS, Javascript, and SvelteKit for the frontend and Flask + Firebase for the backend and authentication. We deployed the website with GitHub pages, and users can host the flask server locally if a user wants to try PropertyProber. sveletekit, js, python, blood, sweat, tears.

## Challenges we ran into

One challenge was implementing user authentication. We found plenty of edge cases to consider for our application to be fully secure. In addition, we found it hard to navigate the complexity of features that need to be considered for a real estate property in general. This made making our prediction models provide actually relevant predictions more difficult, as there were a lot of potential predictors to consider. In addition, it was hard to get good results from fine-tuning existing object detection models. We also had some issues giving our generative AI models the proper context for helpful and relevant reports.

## Accomplishments that we're proud of

We're proud that we managed to implement a wide range of technologies in such a short amount of time. We managed to include AR, maps, computer vision, condition prediction, property value prediction, and environmental impact + narrative report generation.

## What we learned

We learned a ton about computer vision, LLMs, SvelteKit, authentication with Firebase, augmented reality in the browser, and the Google Maps API.

## What's next for PropertyProber

Incorporating more data to allow for better model performance and accuracy, getting feedback for the UI/UX, and scaling up resources to handle more users.
