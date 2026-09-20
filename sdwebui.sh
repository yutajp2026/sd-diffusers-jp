#!/bin/bash
set -euo pipefail

echo "Pythonをインストールしています..."
sudo apt update
sudo apt install -y python3 python3-pip python3-venv

if [ ! -d ".venv" ]; then
    echo "仮想環境を作成しています..."
    python3 -m venv .venv
fi

source .venv/bin/activate
echo "pipを更新しています..."
python -m pip install --upgrade pip

mkdir -p ~/sd_cache
export TMPDIR=~/sd_cache

echo "パッケージをインストールしています..."
pip install -r requirements.txt

echo "WebUIを起動しています..."
python main.py
