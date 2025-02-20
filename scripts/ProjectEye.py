import moondream as md
import cv2
from PIL import Image
from scripts.piper_tts import PiperTTS
from scripts import *

class Projecteye:

    def __init__(self):
        self.model = md.vl(model='Model/moondream_vlm/moondream-0_5b-int8.mf.gz')
        self.image = Image.open("test_files/street.jpg")
        self.encoded_image = self.model.encode_image(self.image)
        
    def caption(self):
        q = Audiostt()
        try:
            query = q.mainSTT()
            print("Query:", query)
        
            if "help" in query or "help me" in query:
                e = Email()
                e.send_email()
                return
            
            if not query.strip():
                print("Error: No query detected")
                return None
            
            try:
                answer = self.model.query(self.encoded_image, query)["answer"]
                print("Answer:", answer)
                return answer
            
            except Exception as e:
                print(f"Error: {e}")
                return None
            
        except Exception as e:
            print(f"Error: {e}")
            return None
        

    def tts(self):
        caption = self.caption()
        if caption:
            print("Caption:", caption)
            tts_engine = PiperTTS() 
            try: 
                tts_engine.run_tts(caption)
            except Exception as e:
                print(f"Error: TTS failed: {e}")
        else:
            print("Error: No caption detected")
