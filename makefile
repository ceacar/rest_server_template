SHELL := /bin/bash
tester_version = 1.0.0
project_name = blazing_potato
service_port = 35555
server_ip = localhost

run:
	(source setenv;\
	export PORT=$(service_port);\
	export SERVER_IP=$(service_ip);\
	python ./run.py)
install:
	(ls ./venv_py3 >/dev/null 2>&1|| virtualenv -p $$(which python3) venv_py3;\
	  source setenv;\
	  cat ./misc/requirement.txt | awk '{print "pip install",$$0}' | bash)
utest:
	(source setenv;\
	pytest -vv ./$(project_name)/tests/utests/test*.py;\
	py.test --cov-report term-missing --cov=$(project_name) ./$(project_name)/;)
itest:
	(source setenv;\
	pytest -vv ./$(project_name)/tests/itests/itest.py)

locust:
	(source setenv;\
	cd scrap_cacher/tests/loadtests;\
	locust --host=$(service_ip):$(service_port))

