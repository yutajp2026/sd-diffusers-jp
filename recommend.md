# Stable Diffusionに興味を持った方へ
これらのアプリには様々な機能が備わっており、本ソフトで使用したモデルを流用できます。上から順に使いやすいです。
## [InvokeAI](https://invoke.ai/start-here/installation/)
最も使いやすく、本ソフトとのモデルの共有もしやすいです。
### モデル使用
モデルパスに入力
## [SwarmUI](https://swarmui.net/)
事前に必要なものもないので使いやすいです(一部OS)。Windows版はWebUIにもGUIにもなります。
### モデル使用
Models内のStable-diffusionにコピー
## [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
公式の説明通りにインストールしようとすると必ず詰むので独自に説明します。
### Windowsへのインストール
1. [Python3.10.6](https://www.python.org/downloads/release/python-3106/)をインストール
2. [VC Regist](https://learn.microsoft.com/ja-jp/cpp/windows/latest-supported-vc-redist?view=msvc-170)がない場合はインストール
3. `winget install --id Git.Git -e --source winget`コマンドでgitをインストール
4. `git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git`コマンドでリポジトリをクローン
5. `webui-user.bat`の内容を編集して下記に変更
```
@echo off
rem 他のバージョンのPythonを使わないようにするために記載する初期パス(必要に応じて削除または変更)
set PYTHON="C:\Users\%username%\AppData\Local\Programs\Python\Python310\python.exe

rem Nvidia GPUがない場合は"--use-cpu all --precision full --no-half --skip-torch-cuda-test"を代入
set COMMANDLINE_ARGS=

rem 詰み防止のため
set STABLE_DIFFUSION_REPO=https://github.com/w-e-w/stablediffusion.git

call webui.bat
```
6. `webui-user.bat`を実行
7. 6の途中でClipをインストールできないエラーが発生するので`venv\Scripts\pip.exe install git+https://github.com/openai/CLIP.git`コマンドを実行
8. もう一度`webui-user.bat`を実行
### モデル使用
Models内のStable-Diffusionにコピー(ただし本ソフトと同じモデルが自動ダウンロードされます)
## [ComfyUI](https://comfy.org/download) 
アプリ版ですがワークフローの知識が必要なため上級者向けです。
### モデル使用
Models内のdiffusion_modelsにコピー
