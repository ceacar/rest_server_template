SHELL := /bin/bash
tester_version = 1.0.0
project_name = simple_server

run:
	(source setenv;\
	python ./run.py)
install:
	(ls ./venv_py3 >/dev/null 2>&1|| virtualenv -p $$(which python3) venv_py3;\
	  source setenv;\
	  cat ./misc/requirement.txt | awk '{print "pip install",$$0}' | bash)
utest:
	(source setenv;\
	pytest -vv ./simple_server/tests/utests/;\
	py.test --cov-report term-missing --cov=simple_server ./simple_server/;)
itest:
	(source setenv;\
	python ./simple_server/tests/itests/itest.py && echo "itest passed")
