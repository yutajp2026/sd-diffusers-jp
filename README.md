# Stable Diffusion With Diffusers JP
画像生成AIであるStable Diffusionを簡単に使えるようにしたアプリ。

# 特徴
- Gradioを使ったWebUI(Windowsのみ自動でブラウザを開く)
- ワンクリックで実行
- txt2imgとimg2img
- 日本語プロンプト対応
- 推論ステップ数の指定
- diffusersを使用
- デバイスを自動選択(CPU、Nvidia GPU)
- Stable Diffusion 1.5を自動ダウンロード
- モデル変更(モデルへのパスを入力するだけ)

# インストール
## Windows
Releasesにインストーラを年内公開
## Linux
1. `sudo apt-get install git`でgitをインストール
2. `git clone https://github.com/yutajp2026/sd-diffusers-jp.git`でこのリポジトリをクローン
3. `cd sd-diffusers-jp`でスクリプトディレクトリに移動
4. `bash sdwebui.sh`で実行 ⚠️linuxの場合は自動でブラウザを開きません
5. `git pull`でアップデート

# Stable Diffusionに興味を持った方へ
これらのアプリには様々な機能が備わっており、本ソフトで使用したモデルを流用できます。上から順に使いやすいです。
### [InvokeAI](https://invoke.ai/start-here/installation/)
モデル使用: モデルパスに入力
### [SwarmUI](https://swarmui.net/)
モデル使用: Models内のStable-diffusionにコピー
### [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
必要なもの: README、issues参照

モデル使用: Models内のStable Diffusionにコピー(ただし本ソフトと同じモデルが自動ダウンロードされます)
### [ComfyUI](https://comfy.org/download) 
必要なもの: ワークフローの知識

モデル使用: Models内のdiffusion_modelsにコピー
