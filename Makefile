all: install

install:
	pipenv install

run:
	pipenv run python src/main.py
