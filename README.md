![site logo](./core/static/core/media/lbwhite.svg)

# Prerequisites
* Ubuntu 20.04 LTS
* Python version 3.8
* MySQL version 8.0
* Docker version 24.0.2

# Installation guide

## Install dependencies:
### Ubuntu 20.04
```
$ (sudo) apt-get install build-essential python3 python3-pip python3-dev python3-setuptools python3-virtualenv libxml2-dev libxslt1-dev python3-dev libpq-dev libffi-dev libssl-dev
```

### Install requirements in a virtual environment
```
$ python3 -m venv virtualenv
$ virtualenv /path/to/venv
$ source /path/to/venv/bin/activate
(venv)$ pip install -r requirements.txt
```

## Option 1: Running the Django app on Docker
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

## Option 2: Running the Django app locally

### Setup Website
#### Create db

`cat setup_mysql.sql | mysql -h localhost -u root -p`

#### Migrate db

`python3 manage.py migrate`

Reach out to one of the collaborators and request for the environment variables. The app will not run without the required environment variables

`echo "your environment variables" >> .env`

### Start development server locally

`python3 manage.py runserver`

# License
Licensed under the [3-clause BSD license](https://en.wikipedia.org/wiki/BSD_licenses#3-clause_license_.28.22Revised_BSD_License.22.2C_.22New_BSD_License.22.2C_or_.22Modified_BSD_License.22.29)
