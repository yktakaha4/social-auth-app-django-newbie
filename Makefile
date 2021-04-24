#!/usr/bin/make -f

.PHONY: migrate
migrate:
	poetry run ./manage.py migrate

.PHONY: runserver
runserver:
	poetry run ./manage.py runserver

.PHONY: dev
dev: migrate runserver
