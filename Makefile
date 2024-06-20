install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
		
format:
	black *.py mylib/*py
	
lint:
	pylint --disable=R,C *.py mylib/*py
	
test:
	python -m pytest -vv --cov=calCli.py --cov=mylib test/test_*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile
	
all: install lint test