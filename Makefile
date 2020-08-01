setup:
	poetry install

gen_requirements:
	poetry export -f requirements.txt >requirements.txt

gen_requirements_dev:
	poetry export --dev -f requirements.txt >requirements-dev.txt

test:
	tox

run:
	docker-compose run monitor
