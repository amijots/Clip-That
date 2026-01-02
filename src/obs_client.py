import obsws_python as obs
import os 

class OBSController:
    def __init__(self):
        self.client = obs.ReqClient(
            host=os.getenv("OBS_HOST"),
            port=int(os.getenv("OBS_PORT")),
            password=os.getenv("OBS_PASSWORD")
        )

        try:
            self.client.start_replay_buffer()
            print("✅ Replay Started!")
        except Exception as e:
             print(f"❌ Error triggering OBS: {e}")
        
    def save_replay(self):
        try:
            self.client.save_replay_buffer()
            print("✅ Replay Saved!")
        except Exception as e:
             print(f"❌ Error triggering OBS: {e}")
