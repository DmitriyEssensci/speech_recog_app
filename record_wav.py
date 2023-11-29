import pyaudio, wave
from datetime import datetime

now = datetime.now() 
current_time = now.strftime("%H:%M")
def record_wav():
    save_dir = 'wav/'
    channels = 2
    frame_rate = 44100
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=channels, rate=frame_rate, input=True, frames_per_buffer=1024, input_device_index=3)
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

    sound_file = wave.open('wav/my_wav.wav', 'wb')
    sound_file.setnchannels(channels)
    sound_file.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(frame_rate)
    sound_file.writeframes(b''.join(frames))
    sound_file.close()

def set_micro():
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')

    for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))


#set_micro()
record_wav()