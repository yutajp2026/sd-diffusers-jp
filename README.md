# Stable Diffusion With Diffusers JP
画像生成AIであるStable Diffusionを簡単に使えるようにしたアプリ。使いやすさを重視。

# 特徴
- Gradioを使ったWebUI(Windowsのみ自動でブラウザを開く)
- ワンクリックで実行
- txt2imgとimg2img
- 日本語プロンプト対応
- 推論ステップ数の指定
- diffusersを使用
- デバイスを自動選択(CPU、Nvidia GPU)
- 生成時間最長約9分(推論ステップ数10、CPUの場合)
- Stable Diffusion 1.5を自動ダウンロード
- モデル変更

# インストール
## Windows
Releasesにインストーラを年内公開
## Linux
1. `sudo apt-get install git`でgitをインストール
2. `git clone https://github.com/yutajp2026/sd-diffusers-jp.git`でこのリポジトリをクローン
3. `cd sd-diffusers-jp`でスクリプトディレクトリに移動
4. `bash sdwebui.sh`で実行
5. `git pull`でアップデート

# Stable Diffusionに興味を持った方へ
これらのアプリには様々な機能が備わっており、本ソフトでダウンロードしたモデルを流用できます。上から順に使いやすいです。
- [InvokeAI](https://invoke.ai/start-here/installation/) (モデルパスに本ソフトでダウンロードしたモデルへのパスを入力)
- [SwarmUI](https://github.com/mcmonkeyprojects/SwarmUI) (Models\Stable-diffusionにモデルをコピー)
- [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) (同じモデルが自動でダウンロードされます)
- [ComfyUI](https://comfy.org/download) (モデルフォルダのdiffusion_modelsにコピー)
