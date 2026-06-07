Set-StrictMode -Version Latest
Remove-Item -Recurse -Force .venv -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force __pycache__ -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force .pytest_cache -ErrorAction SilentlyContinue
