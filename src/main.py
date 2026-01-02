import yaml
from dotenv import load_dotenv
from obs_client import OBSController
from audio_monitor import AudioMonitor

# 1. Load Secrets & Config
load_dotenv()
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

# 2. Initialize OBS
obs = OBSController()

# 3. Define what happens when shouting is detected
def on_shouting_detected():
    obs.save_replay()

# 4. Start Monitoring
if __name__ == "__main__":
    monitor = AudioMonitor(config, trigger_callback=on_shouting_detected)
    try:
        monitor.start_listening()
    except KeyboardInterrupt:
        print("\nStopping...")
        obs.disconnect()