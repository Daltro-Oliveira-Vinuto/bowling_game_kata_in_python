all: test lint mypy

test:
	pytest -v

lint:
	pylint "sources/bowling_game.py"
	pylint "sources/main.py"

mypy:
	mypy "sources/bowling_game.py"
	mypy "sources/main.py"


debug:
	python -m pdb "sources/main.py"

run:
	python "sources/main.py"