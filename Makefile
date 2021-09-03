PYTHON_BIN=venv/bin/python
PYPI_REPOSITORY_URL=https://pypi.magazineluiza.com.br/pypi/

.PHONY: build
build: venv
	$(PYTHON_BIN) setup.py sdist

venv:
	@python3 -m pip install virtualenv
	@python3 -m virtualenv venv
	@. venv/bin/activate
	$(PYTHON_BIN) -m pip install --upgrade pip
	$(PYTHON_BIN) -m pip install -r requirements/develop.txt

publish:
	$(PYTHON_BIN) -m twine upload --repository-url $(PYPI_REPOSITORY_URL) dist/*
