#!/bin/bash
set -euo pipefail

if ! command -v python3 >/dev/null 2>&1; then
	sudo apt update
	sudo apt install -y python3 python3-pip
fi

if [[ ! -x .venv/bin/python ]]; then
	if ! python3 -m venv .venv; then
		python_version="$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
		sudo apt update
		sudo apt install -y "python${python_version}-venv"
		rm -rf .venv
		python3 -m venv .venv
	fi
fi

source .venv/bin/activate
python -m pip install --upgrade pip

mkdir -p ~/pip_cache
export TMPDIR=~/pip_cache

pip install gradio diffusers transformers translate
pip install torch==2.12.0 torchvision==0.27.0 --index-url https://download.pytorch.org/whl/cu126

python main.py
