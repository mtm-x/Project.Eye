import subprocess
import os
import datetime

PIPER_PATH = "piper/./piper"
MODEL_PATH = "Model/TTS/en_US-amy-low.onnx"
DATE = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
OUT = 0  

class PiperTTS:
    def __init__(self):
        self.OUTPUT_PATH = ""  

    def run_tts(self, text):
        
        global OUT  
        if not os.path.exists("output"):
            os.makedirs("output")
        while os.path.exists(f"output/output_{OUT}.wav"):
            OUT += 1
        self.OUTPUT_PATH = f"output/output_{OUT}.wav"
        try:
            subprocess.run(
                [PIPER_PATH, "--model", MODEL_PATH, "--output_file", self.OUTPUT_PATH],
                input=text.encode(),
                check=True
            )
        except subprocess.CalledProcessError:
            print("Error: TTS failed")
            return
        print(f"🔊 TTS output saved to {self.OUTPUT_PATH}")
        self.play_tts()  

    def play_tts(self):
        try:
            if self.OUTPUT_PATH:
                subprocess.run(["aplay", self.OUTPUT_PATH], check=True)
        except subprocess.CalledProcessError:
            print("Error: Playback failed")
            return
        print(f"🔊 TTS playback complete at {DATE}")

