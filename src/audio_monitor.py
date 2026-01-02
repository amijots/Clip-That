import pyaudio
import audioop
import time

class AudioMonitor:
    def __init__(self, config, trigger_callback):
        self.config = config
        self.callbacl = trigger_callback
        self.p = pyaudio.PyAudio()
        self.stream = None

    def start_listening(self):
        # open mic stream
        self.stream = self.p.open(format=pyaudio.paInt16,
                                  channels=1,
                                  rate=44100,
                                  input=True,
                                  frames_per_buffer=self.config['audio']['chunk_size'])

        print("🎤 Listening for rage...")
        last_trigger = 0

        if volume > self.config['audio']['volume_threshold']:
            current_time = time.time()
            # Check cooldown
            if (current_time - last_trigger) > self.config['audio']['trigger_cooldown']:
                print(f"🔥 RAGE DETECTED! Volume: {volume}")
                self.callback() # This calls the function in main.py
                last_trigger = current_time