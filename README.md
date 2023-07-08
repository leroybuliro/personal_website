# Overview
## Application and Data
Python, Django, MySQL, HTML5, CSS3, jQuery

## DevOps
Git, GitHub Actions, Docker, Jira

## Requirements
* Python version 3.8.10
* MySQL version 8.0
* Docker version 24.0.2

<br><br>

# Project setup
## Running the python app on docker
In the terminal, change directory to the personal_website directory then run the command below to start the app container.

`docker compose up -d`

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
