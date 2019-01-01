.PHONY: release test


clean:
	rm -rf dist/


prepforrelease:
	pip install --upgrade twine setuptools wheel


testrelease:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*


release: artifacts
	twine upload --repository-url https://upload.pypi.org/legacy/ dist/*


artifacts:
	python setup.py sdist


test:
	pytest


init:
	pip install -r requirements.txt


test-v:
	pytest -v
