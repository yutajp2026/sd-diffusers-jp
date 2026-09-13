#!/usr/bin/env bash
set -euo pipefail

if ! command -v python3 >/dev/null 2>&1; then
	sudo apt-get update
	sudo apt-get install -y python3 python3-venv python3-pip
fi

python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip

pip install gradio diffusers transformers translate
pip install torch==2.12.0 torchvision==0.27.0 --index-url https://download.pytorch.org/whl/cu126

exec python main.py
