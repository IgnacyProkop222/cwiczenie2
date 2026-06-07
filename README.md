# cwiczenie2

Quick start
-----------

1. Create a virtual environment and install dependencies (Linux/macOS):

	python3 -m venv .venv
	source .venv/bin/activate
	pip install -r requirements.txt

	On Windows (PowerShell):

	python -m venv .venv
	.\.venv\Scripts\Activate.ps1
	pip install -r requirements.txt

2. Run tests:

	.venv\Scripts\python -m pytest -q

CI and scripts
--------------

This repo includes helper scripts under `scripts/` for both POSIX shell and
PowerShell. CI is configured in `.github/workflows/ci.yml` and runs Black
format check, pylint, and pytest.

Common commands (PowerShell):

	.\scripts\create_venv.ps1
	.\scripts\format.ps1
	.\scripts\format_check.ps1
	.\scripts\lint.ps1
	.\scripts\test.ps1
	.\scripts\clean.ps1

On Unix-like systems you can run the sh scripts in `scripts/` (they call
the tools directly).

Notes
-----

- Black is configured with line-length 88 in `pyproject.toml`.
- Pylint configuration is in `.pylintrc` and also uses max-line-length 88.

