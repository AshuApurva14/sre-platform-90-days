test:
	python -m pytest 05-capstone/tests

run:
	python 05-capstone/application/main.py

docker-build:
	docker build -t sre-demo:local 05-capstone
