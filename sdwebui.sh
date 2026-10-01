#!/bin/bash
set -euo pipefail

if ! python3 --version >/dev/null 2>&1; then
    echo "エラー: python3 を実行できません。Python 3 をインストールしてください。" >&2
    exit 1
fi

if [ ! -d ".venv" ]; then
    echo "仮想環境を作成しています..."
    python3 -m venv .venv
fi

source .venv/bin/activate
if ! python --version >/dev/null 2>&1; then
    echo "エラー: 仮想環境内の python を実行できません。" >&2
    exit 1
fi

echo "pipを更新しています..."
python -m pip install --upgrade pip

mkdir -p ~/sd_cache
export TMPDIR=~/sd_cache

echo "パッケージをインストールしています..."
pip install -r requirements.txt

echo "WebUIを起動しています..."
python main.py
