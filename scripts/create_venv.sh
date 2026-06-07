#!/bin/bash
set -e
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# On Windows (PowerShell) use:
# python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt
