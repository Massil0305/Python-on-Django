# Convert-Digits-to-English-words-with-Python-Django


This Repository installs :

- `Django`
- `Postgres`

It deploys a Web Service to run a Python Script

## Requirements:

- `Docker`
- `Docker compose`
- `Python 3`

## Usage:

1- Create Django project

- docker-compose run web django-admin startproject composeexample .
 
2- Copy confi file to the project:

- cp CONFIG/* composeexample

3- Start Prject:
- docker-compose up

## Note:

Somehow "RUN pip install requests" isn't executed from Dockerfile

Please, execute manually the command before launching the browser :

docker exec -it \`docker ps -a | grep web | awk {'print $1'}\` python3 -m pip install requests 

Then launch the browser at http://127.0.0.1:8000

## Author
Salah Lahlou
