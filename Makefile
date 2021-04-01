install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python -m pip install --user dist/*.whl

package-reinstall:
	python -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 brain_games
