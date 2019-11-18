PYTHON_BIN ?= python

format: isort black

black:
	'$(PYTHON_BIN)' -m black --target-version py36 --exclude '/(\.git|\.hg|\.mypy_cache|\.nox|\.tox|\.venv|_build|buck-out|build|dist|node_modules|webpack_bundles)/' .

isort:
	'$(PYTHON_BIN)' -m isort -rc cpb_s00
	'$(PYTHON_BIN)' -m isort -rc cpb_s00_api
