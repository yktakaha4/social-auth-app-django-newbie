#!/usr/bin/make -f

.PHONY: install
install:
	poetry install

.PHONY: migrate
migrate:
	poetry run ./manage.py migrate

.PHONY: runserver
runserver:
	poetry run ./manage.py runserver

.PHONY: shell
shell:
	poetry run ./manage.py shell_plus

.PHONY: dev
dev: migrate runserver
