## POC for the AI SUMMARIZATION

This project is POC implementation of AI Summarization that can be generated through utilizing OpenAI API to communicate with the GPT models. The project uses Python Flask framework to create endpoints for generating summaries with GPT models and concurrently designing the front-end to display the results.

## Running the app

There are two ways to run the app.
- Deploying with docker container.
- Running the standalone app as a python flask app.

You need an OPENAI_KEY to communicate to the GPT models irrespective of the option you choose to run the app. Once you have your key, do the following on CLI:

- Git clone this repository by
`git clone https://github.com/sakib1486/summryze.git`

- Navigate into the directory cloned:
`cd summryze`

- Create a new file named .env and paste the contents of the .env.example file.

- Copy paste your OPENAI_KEY in the .env file where marked.


# Deploying with Docker Container

If you do not have docker installed, please go to the official login page, and install docker desktop and run it. After you have succesfully installed docker desktop, follow the steps below in the terminal/powershell:

- First, we build the docker image with necessary libraries by hitting:
`docker build -t MY_FLASK_APP .`
We can replace MY_FLASK_APP with whatever name we like.

- Finally, run the app by:
`docker run -p 5000:5000 MY_FLASK_APP`

The chat page would be available at **localhost:5000/chat**.

# Running from the CLI

If you have Python and Flask installed in your machine, you can directly run the app from the CLI. The first step is to Git clone this repo again. Then move to the directory of the cloned repo on the CLI.

If you have python only, please run the following first,

`pip install --no-cache-dir -r requirements.txt`

After the pip ran successfully, hit:

`flask run`

The app should be available at **localhost:5000/chat**.
