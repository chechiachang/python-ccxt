all: install

install:
	pipenv install

main:
	pipenv run python src/main.py
