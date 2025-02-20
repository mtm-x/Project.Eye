import time
from scripts import *

def main():
    eye = Projecteye()

    try:
        while True:
            eye.tts()
            time.sleep(3)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
