import json
import pyaudio
from vosk import Model, KaldiRecognizer


class Audiostt:
    def __init__(self):
        self.text = ""
        self.MODEL_PATH = "/home/lotus/Downloads/git_projects/ProjectEye/Model/Vosk/vosk-model-small-en-in-0.4"
        self.model = Model(self.MODEL_PATH)

    def speech_to_text(self, duration=5):
        """Captures microphone input and returns transcribed text as a string."""
        recognizer = KaldiRecognizer(self.model, 16000)

        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=16000,
                        input=True,
                        frames_per_buffer=4000)

        print("🎤 Speak now...")
        
        for _ in range(0, int(16000 / 4000 * duration)):  # Capture audio for 'duration' seconds
            data = stream.read(4000)
            if recognizer.AcceptWaveform(data):
                break  # Stop early if speech is recognized

        stream.stop_stream()
        stream.close()
        p.terminate()

        result = json.loads(recognizer.Result())
        return result.get("text", "")

    # Get Transcription
    def mainSTT(self):
        text = self.speech_to_text(duration=10)
        print("\n📝 Transcription:", text)
        return text