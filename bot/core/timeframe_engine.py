import pandas as pd
import numpy as np

class TimeframeEngine:
    def __init__(self, settings):
        self.settings = settings

    def fetch_multi_timeframe(self):
        result = {}
        for tf in self.settings.timeframes:
            result[tf] = self._generate_fake(tf)
        return result

    def _generate_fake(self, tf):
        x = np.linspace(1, 100, 200)
        price = 30000 + np.sin(x) * 100
        return pd.DataFrame({
            "open": price-5,
            "high": price+10,
            "low": price-15,
            "close": price,
            "volume": np.random.randint(50,150,len(price))
        })
