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

## インストール
## Windows
Releasesにインストーラを年内公開
## linux
1. `sudo apt-get install git`でgitをインストール
2. `git clone https://github.com/yutajp2026/sd-diffusers-jp.git`でこのリポジトリをクローン
3. `cd sd-diffusers-jp`でスクリプトディレクトリに移動
4. `bash sdwebui.sh`で実行

# Stable Diffusionに興味を持った方へ
これらのアプリには様々な機能が備わっています。
- [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
- [InvokeAI](https://invoke.ai/start-here/installation/)
- [ComfyUI](https://comfy.org/download)
- [SwarmUI](https://github.com/mcmonkeyprojects/SwarmUI)
