.PHONY: install test lint run docker-up validate
install:
	pip install -r requirements-dev.txt
test:
	pytest -q
lint:
	ruff check app tests
run:
	uvicorn app.main:app --reload --port 8080
docker-up:
	docker compose up --build
validate:
	python -m compileall -q app tests
