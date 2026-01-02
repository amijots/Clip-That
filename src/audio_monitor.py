import pyaudio
import audioop
import time

class AudioMonitor:
    def __init__(self, config, trigger_callback):
        self.config = config
        self.callback = trigger_callback
        self.p = pyaudio.PyAudio()
        self.stream = None

    def start_listening(self):
        # open mic stream
        self.stream = self.p.open(format=pyaudio.paInt16,
                                  channels=1,
                                  rate=44100,
                                  input=True,
                                  frames_per_buffer=self.config['audio']['chunk_size'])

        print("🎤 Listening for shouting...")
        last_trigger = 0

        while True:
            data = self.stream.read(self.config['audio']['chunk_size'])
            # Calculate volume (RMS)
            rms = audioop.rms(data, 2) 
            
            # Simple normalization logic (adjust based on your mic)
            volume = rms / 20000  
            print(rms, volume)
            if volume > self.config['audio']['volume_threshold']:
                current_time = time.time()
                # Check cooldown
                if (current_time - last_trigger) > self.config['audio']['trigger_cooldown']:
                    print(f"🔥 SHOUTING DETECTED! Volume: {volume}")
                    self.callback() # This calls the function in main.py
                    last_trigger = current_time