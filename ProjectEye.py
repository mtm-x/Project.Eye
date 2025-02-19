import moondream as md
import cv2
from PIL import Image
from scripts.piper_tts import PiperTTS

class Projecteye():

    def __init__(self):
        self.model = md.vl(model='Model/moondream_vlm/moondream-0_5b-int8.mf.gz')
        self.image = Image.open("test_files/street.jpg")
        self.encoded_image = self.model.encode_image(self.image)

    def caption(self):
        caption = self.model.caption(self.encoded_image)["caption"]
        return caption

    def tts(self):
        caption = self.caption()
        tts_engine = PiperTTS()  
        tts_engine.run_tts(caption) 


if __name__ == "__main__":
    eye = Projecteye()
    eye.tts()


