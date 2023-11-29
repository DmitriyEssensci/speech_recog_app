import pyaudio, wave
from datetime import datetime

now = datetime.now() 
current_time = now.strftime("%H:%M")

channels = 1
frame_rate = 44100
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=channels, rate=frame_rate, input=True, frames_per_buffer=1024)
frames = []
try:
    while True:
        data = stream.read(1024)
        frames.append(data)
except KeyboardInterrupt:
    pass

stream.stop_stream()
stream.close()
p.terminate()

sound_file = wave.open(current_time+'my_wav.wav', 'wb')
sound_file.setnchannels(channels)
sound_file.setsampwidth(p.get_sample_size(pyaudio.paInt16))
sound_file.setframerate(frame_rate)
sound_file.writeframes(b''.join(frames))
sound_file.close()