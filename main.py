from diffusers import StableDiffusionPipeline, StableDiffusionImg2ImgPipeline
import torch
from translate import Translator
import os
import gradio as gr
import webbrowser
import platform
from PIL import Image
import time
import logging

logging.basicConfig(level=logging.INFO)
sd_file = os.path.join(os.getcwd(), 'v1-5-pruned-emaonly.safetensors')

if not os.path.exists(sd_file):
    print("モデルをダウンロードしています...")
    url = 'https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.safetensors'
    torch.hub.download_url_to_file(url, sd_file, hash_prefix=None, progress=True)
    print("モデルのダウンロードが完了しました。")

if os.path.exists('model_settings.txt'):
    with open('model_settings.txt', 'r') as f:
        model_file = f.read().strip()
else:
    model_file = sd_file

if torch.cuda.is_available():
    print("GPUが利用可能です。CUDAを使用します。")
    device = 'cuda'
else:
    print("GPUが利用できません。CPUを使用します。")
    device = 'cpu'

honyaku = Translator('en','ja').translate

with gr.Blocks() as demo:
    gr.Markdown("# Stable Diffusion 日本語プロンプト対応版")
    with gr.Tab("txt2img"):
        gr.Markdown("Txt2Imgタブでは、テキストから画像を生成できます。")
        def txt2img(prompt, steps):
            pipe1 = StableDiffusionPipeline.from_single_file(model_file).to(device)
            img = pipe1(honyaku(prompt), num_inference_steps=steps).images[0]
            gr.Info("生成が完了しました。")
            return img

        prompt_input = gr.Textbox(label="プロンプト")
        steps_input = gr.Number(label="推論ステップ数", value=10, precision=0)
        txt2img_btn = gr.Button("生成")
        image_output = gr.Image()
        txt2img_btn.click(fn=txt2img, inputs=[prompt_input, steps_input], outputs=image_output)
        
    with gr.Tab("img2img"):
        gr.Markdown("Img2Imgタブでは、画像をプロンプトに基づいて編集できます。")
        def img2img(image, prompt, steps):
            pipe2 = StableDiffusionImg2ImgPipeline.from_single_file(model_file).to(device)
            img0 = Image.open(image)
            img = pipe2(honyaku(prompt), image=img0, num_inference_steps=steps).images[0]
            gr.Info("生成が完了しました。")
            return img
        image_input = gr.Image(label="入力画像", type="filepath")
        prompt_input = gr.Textbox(label="プロンプト")
        steps_input = gr.Number(label="推論ステップ数(実際のステップ数は入力値の8割になります)", value=10, precision=0)
        img2img_btn = gr.Button("生成")
        image_output = gr.Image()
        img2img_btn.click(fn=img2img, inputs=[image_input, prompt_input, steps_input], outputs=image_output)
    with gr.Tab("メニュー"):
        gr.Markdown("## サーバー")
        def quit():
            gr.Info("アプリケーション終了。タブは手動で閉じてください。")
            time.sleep(1)
            os._exit(0)
        quit_btn = gr.Button("終了")
        quit_btn.click(fn=quit, inputs=[], outputs=[])
        gr.Markdown("## モデル設定")
        gr.Markdown("下記モデルパスは、他のソフトでモデルを使うときのストレージの節約に役に立ちます。デフォルトは " + os.path.join(os.getcwd(), sd_file))
        def change_model(model_path):
            global model_file
            model_file = model_path
            if model_path == sd_file:
                gr.Info("デフォルトのモデルが選択されました。")
                os.remove('model_settings.txt') if os.path.exists('model_settings.txt') else None
                return
            with open('model_settings.txt', 'w') as f:
                f.write(model_file)
            gr.Info("モデルが変更されました。新しいモデルのパス: " + model_file)
        model_input = gr.Textbox(label="モデルのパス(クオーテーションやダブルクオーテーション不要)", value=model_file)
        change_model_btn = gr.Button("モデル変更")
        change_model_btn.click(fn=change_model, inputs=[model_input], outputs=[])

if platform.system() == "Windows":
    webbrowser.open("http://localhost:7860")
else:
    print("ブラウザで以下のURLを開いてください。")

demo.launch()