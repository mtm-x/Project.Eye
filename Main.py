import threading
import time
from scripts import *

def main():
    eye = Projecteye()  
    e = Email()

    while True:
        q = Audiostt()
        query = q.mainSTT()
        print("Query:", query)
        eye.tts()
        time.sleep(3)
main()
