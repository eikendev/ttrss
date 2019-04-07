DIR_SRC=./ttrss
DIR_TEST=./test

.PHONY: all
all: compile

.PHONY: compile
compile:
	@echo "Nothing to compile."

.PHONY: clean
clean:
	find -type d -name '__pycache__' -exec rm -rf {} +;
	find -type d -name '.pytest_cache' -exec rm -rf {} +;
	find -type d -name '.mypy_cache' -exec rm -rf {} +;
	rm -rf ${DIR_TEST}/.cache
	rm -f tags

.PHONY: run
run:
	@python3 -m ttrss

.PHONY: test
test:
	@python3 -m pytest -vv

.PHONY: tags
tags:
	ctags -R --extra=+f ${DIR_SRC}

.PHONY: flake
flake:
	@flake8 --ignore=E501 ${DIR_SRC}

.PHONY: vulture
vulture:
	@vulture-3 --exclude version.py ${DIR_SRC} && echo 'No dead code found.'

.PHONY: check
check:
	@mypy --ignore-missing-imports ${DIR_SRC}
