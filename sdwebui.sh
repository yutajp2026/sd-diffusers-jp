#!/bin/bash
set -euo pipefail

sudo apt update
sudo apt install -y python3 python3-pip python3-venv

if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi

source .venv/bin/activate
python -m pip install --upgrade pip

mkdir -p ~/sd_cache
export TMPDIR=~/sd_cache

pip install gradio diffusers transformers translate
pip install torch==2.12.0 torchvision==0.27.0 --index-url https://download.pytorch.org/whl/cu126

python main.py
