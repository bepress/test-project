PROJECT :=project
CW :=$(shell pwd)
DATABASE_URL:=sqlite:///./database.sql

install:
	pipenv install -d

shell:
	pipenv shell

test:
	DATABASE_URL=$(DATABASE_URL) pipenv run pytest

lint:
	bin/lint.sh

makemigrations:
	DATABASE_URL=$(DATABASE_URL) pipenv run python manage.py makemigrations

migrate:
	DATABASE_URL=$(DATABASE_URL) pipenv run python manage.py migrate

run:
	DATABASE_URL=$(DATABASE_URL) DEBUG=true pipenv run python manage.py runserver
