import subprocess
import os

PIPER_PATH = "piper/./piper"
MODEL_PATH = "Model/TTS/en_US-amy-low.onnx"
OUTPUT_PATH = "output/output.wav"

def run_tts(text):
    subprocess.run(
    [PIPER_PATH, "--model", MODEL_PATH, "--output_file", OUTPUT_PATH],
    input=text.encode(),  
    check=True
)
