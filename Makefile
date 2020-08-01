setup:
	poetry install

gen_requirements:
	poetry export --without-hashes -f requirements.txt >requirements.txt

gen_requirements_dev:
	poetry export --without-hashes --dev -f requirements.txt >requirements-dev.txt

test:
	tox

run:
	docker-compose run monitor
