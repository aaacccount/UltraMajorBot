class Settings:
    def __init__(self):
        self.timeframes = ["15m", "1h", "4h", "1d", "1w"]
        self.symbol = "BTCUSDT"
        self.initial_balance = 1000
        self.commission = 0.0004
        self.refresh_seconds = 5
        self.use_macd = True
        self.use_vwap = True
        self.use_atr_dynamic = True
        self.use_fvg = True
        self.use_ob = True
        self.use_divergence = True
