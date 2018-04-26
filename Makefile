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
