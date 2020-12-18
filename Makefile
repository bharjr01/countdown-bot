.PHONY: all clean install test

all: clean install test

ifeq (, $(shell which pipenv))
$(error "No pipenv in $(PATH), consider doing brew install pipenv")
endif

clean:
	pipenv --rm || :

install:
	pipenv sync -d

test:
	pipenv run python -m unittest discover
	pipenv run mypy -p src -p test
