from diffusers import StableDiffusionPipeline, AutoPipelineForImage2Image
import torch
from translate import Translator
import os
import gradio as gr
import webbrowser
import platform
from diffusers.utils import make_image_grid, load_image

model_file = 'v1-5-pruned-emaonly.safetensors'

if not os.path.exists(model_file):
    url = 'https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.safetensors'
    torch.hub.download_url_to_file(url, model_file, hash_prefix=None, progress=True)

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
        pipe = StableDiffusionPipeline.from_single_file(model_file).to(device)

        def txt2img(prompt, steps):
            img = pipe(honyaku(prompt), num_inference_steps=steps).images[0]
            return img

        prompt_input = gr.Textbox(label="プロンプト")
        steps_input = gr.Number(label="推論ステップ数", value=10, precision=0)
        generate_btn = gr.Button("生成")
        image_output = gr.Image()
        generate_btn.click(fn=txt2img, inputs=[prompt_input, steps_input], outputs=image_output)
    with gr.Tab("img2img"):
        gr.Markdown("img2imgは現在サポートされていません。")

if platform.system() == "Windows":
    webbrowser.open("http://localhost:7860")

demo.launch()