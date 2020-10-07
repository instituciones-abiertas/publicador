install: clean
	pip3 install -r requirements.txt

test:
	python3 setup.py test

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

release: clean dist
	python3 setup.py sdist
	python3 setup.py bdist_wheel
	python3 -m twine upload dist/*

dist: clean
	python3 setup.py sdist
	python3 setup.py bdist_wheel
	ls -l dist

.PHONY: install test clean release dist
