import moondream as md
import cv2
from PIL import Image
from scripts.piper_tts import PiperTTS
from scripts import*

class Projecteye():

    def __init__(self):
        self.model = md.vl(model='Model/moondream_vlm/moondream-0_5b-int8.mf.gz')
        self.image = Image.open("test_files/street.jpg")
        self.encoded_image = self.model.encode_image(self.image)
        
    def caption(self):
        q = Audiostt()
        try:
            query = q.mainSTT()
            print("Query:", query)
            if query == "":
                print("No query detected")
                return
        except:
            print("Error: No query detected")
            return
        try:
            answer = self.model.query(self.encoded_image, str(query))["answer"]
            print
            return answer
        except:
            print("Error: No answer detected")
            return
       

    def tts(self):
        caption = self.caption()
        if caption:
            print("Caption:", caption)
            tts_engine = PiperTTS() 
            try: 
                tts_engine.run_tts(caption)
            except:
                print("Error: TTS failed")
                return
        else:
            print("Error: No caption detected")
            return

if __name__ == "__main__":
    eye = Projecteye()
    eye.tts()


