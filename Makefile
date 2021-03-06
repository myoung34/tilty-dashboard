setup:
	poetry install

gen_requirements:
	poetry export --without-hashes -f requirements.txt >requirements.txt

gen_requirements_dev:
	poetry export --without-hashes --dev -f requirements.txt >requirements-dev.txt

bump_version:
	sed -i.bak "s/version = \".*\"/version = \"$(VERSION)\"/g" pyproject.toml
	sed -i.bak "s/version='.*'/version='$(VERSION)'/g" setup.py
	rm pyproject.toml.bak setup.py.bak

test:
	poetry run tox

run:
	docker-compose build
	docker-compose up app

.PHONY: seed
seed:
	rm data || :
	mkdir data || :
	sqlite3 data/tilt.sqlite ".read seed/create.sql"
	bash seed/seed.sh
