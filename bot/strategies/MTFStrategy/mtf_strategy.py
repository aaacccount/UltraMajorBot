from bot.core.timeframe_engine import TimeframeEngine
from bot.core.structure_detector import StructureDetector
from bot.core.signal_fusion import SignalFusion

class MTFStrategy:
    def __init__(self, settings):
        self.settings = settings
        self.engine = TimeframeEngine(settings)
        self.structure = StructureDetector()
        self.fusion = SignalFusion()

    def run_live_loop(self):
        import time
        print("🔥 Live loop started... (CTRL+C to exit)")

        while True:
            try:
                mtf_data = self.engine.fetch_multi_timeframe()
                structure_info = self.structure.detect(mtf_data)
                signal = self.fusion.combine(mtf_data, structure_info)
                print("🔎 Signal →", signal)
            except Exception as e:
                print("⚠️ Error:", e)

            time.sleep(self.settings.refresh_seconds)
