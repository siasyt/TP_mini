.PHONY: setup format lint run

setup:
	python -m pip install -r requirements.txt
	pre-commit install

format:
	black src notebooks
	isort src notebooks

lint:
	ruff check src notebooks
	ruff format --check
	ruff fix --select I --unsafe-fixes
	ruff check --select F401  # imports inutiles
	ruff check --select E --select W
	ruff check --select I
	ruff check --statistics
	ruff check --show-source

run:
	python main.py
	python duckdb_query.py
	duckdb_analysis.ipynb
	mini_dw_tp.ipynb

