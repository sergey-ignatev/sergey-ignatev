# Initial prepares

TERMINAL_CHECK := $(shell if [ -t 0 ] ; then echo terminal; else echo "not a terminal"; fi)

ifneq ($(strip $(shell pwd)),/app)
ifeq ($(strip $(CI)),)

ifeq ($(TERMINAL_CHECK), terminal)
	CMD_PREFIX := docker exec -ti pythontest_web_1
else
	CMD_PREFIX := docker exec -i pythontest_web_1
endif
endif
endif

# Helper command

help:
	@echo 'Test project'
	@echo ''
	@echo 'Commands:'
	@echo '    help - show this message'
	@echo ''
	@echo '    init-admin  - create default superuser (username: admin, password: password)'


# Usability functions

up:
	@docker-compose stop
	@docker-compose up

stop:
	@docker-compose stop


# Project initialization

migrate:
	@$(CMD_PREFIX) python3 db_work/db.py