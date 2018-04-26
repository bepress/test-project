PROJECT :=project
CW :=$(shell pwd)

build_container:
	docker-compose build

shell:
	docker-compose run --rm project /bin/bash

test:
	docker-compose run --rm project pytest

lint:
	docker-compose run --rm project bin/lint.sh

makemigrations:
	docker-compose run --rm project python manage.py makemigrations

migrate:
	docker-compose run --rm project python manage.py migrate

run:
	docker-compose up -d

logs:
	docker-compose logs -f
