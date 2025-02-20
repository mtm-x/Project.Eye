import pyaudio

p = pyaudio.PyAudio()

# List all audio input devices
for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    print(f"Device Index: {i}, Name: {info['name']}, Input Channels: {info['maxInputChannels']}")

p.terminate()
