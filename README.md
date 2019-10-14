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

git clone <url>

cd <Directory>

docker-compose up

## Note:

Somehow "RUN pip install requests" isn't executed from Dockerfile

so before luanch the browser http://127.0.0.1:8000

Please, execute manually the command :

docker exec -it `docker ps -a | grep web | awk {'print $1'}` python3 -m pip install requests

Then Lunch the browser at http://127.0.0.1:8000