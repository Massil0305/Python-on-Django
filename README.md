# Convert-Digit-2-words-with-Python-Django

This Repository installs :

- `Django`
- `Postgres`

It deploys a Web Service to run a Python Script

## Requirements:

- `Docker`
- `Docker compose`
- `Python 3`

## Usage:

1- Clone the Repository :

- git clone https://github.com/Massil0305/Python-on-Django.git

- cd Python-on-Django

2- Create Django project

- docker-compose run web django-admin startproject composeexample .
 
3- Copy confi file to the project:

- cp CONFIG/* composeexample

4- Start Prject:
- docker-compose up

## Note:

Python requests module is required, please, make sure it is installed before launching the browser :

docker exec -it \`docker ps -a | grep web | awk {'print $1'}\` python3 -m pip install requests 

Then launch the browser at http://127.0.0.1:8000

Ensure /etc/hosts points 127.0.0.1 to localhost.


## Acknowledgements:
- https://docs.docker.com/compose/django/ 
- https://www.youtube.com/watch?v=s6Xi7x4G7yg 
- https://www.youtube.com/watch?reload=9&v=ERMRVORGvZM 
- https://www.youtube.com/watch?v=vsdSIe9X8nQ
