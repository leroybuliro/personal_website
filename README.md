# Overview
## Application and Data
Python, Django, MySQL, HTML5, CSS3, jQuery

## DevOps
Git, GitHub Actions, Docker, Jira


<br><br>

# Project setup
## Requirements
* Python version 3.8.10
* MySQL version 8.0
* Docker version 24.0.2

## Getting started

1. clone repository

    `git clone https://githubm/leroysb/reciperealm.git`

2. change directory

    `cd RecipeRealm/`

### Option 1: Running the Django app on Docker
In the terminal, change directory to the personal_website directory then run the command below to start the app container.

<!-- `docker compose up -d` -->
`docker-compose --env-file .env up -d`

Confirm that the container is running using the ps command

`docker ps`

Output similar to the following should appear.

```
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                      NAMES
df784548666d        getting-started     "docker-entrypoint.s…"   2 minutes ago       Up 2 minutes        127.0.0.1:3000->3000/tcp   priceless_mcclintock
```
Use the stop command to stop the container. 

`docker stop <the-container-ids>`

Once the container has stopped, you can remove it by using the rm command.

`docker rm -f <the-container-ids>`

### Option 2: Running the Django app locally

Make a virtual environment

`python3 -m venv virtualenv`

Activate virtual environment

```
source virtualenv/bin/activate # For Linux
source virtualenv/scripts/activate # For Windows
```

Install python3 packages

`pip install -r requirements.txt`

Setup database

`cat setup_mysql.sql | mysql -h localhost -u root -p`

Migrate database

`python3 manage.py migrate`

Reach out to one of the collaborators and request for the environment variables. The app will not run without the required environment variables

`echo "your environment variables" >> .env`

Run server locally

`python3 manage.py runserver`
