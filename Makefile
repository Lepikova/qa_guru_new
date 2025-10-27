help:
	@echo "Makefile commands:"
	@echo "  install     - Установить зависимости"
	@echo "  run_test    - Запустить автотесты"
	@echo "  test_only   - Запустить автотест с меткой only"
	@echo "  linter      - Запустить проверку кода"

install:
	pip install -r requirements.txt

run_test:
	python3 -m pytest -v

linter:
	black .
	isort .
	flake8
