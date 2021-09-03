PYTHON_BIN=venv/bin/python

venv:
	@python3 -m pip install virtualenv
	@python3 -m virtualenv venv
	@. venv/bin/activate
	$(PYTHON_BIN) -m pip install --upgrade pip
	$(PYTHON_BIN) -m pip install -r requirements/develop.txt

run:
	uvicorn --app-dir app app:app --reload
