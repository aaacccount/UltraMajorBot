class MACD:
    def __init__(self, fast=12, slow=26, signal=9):
        self.fast=fast; self.slow=slow; self.signal=signal
    def calculate(self, df):
        df['ema_fast'] = df['close'].ewm(span=self.fast, adjust=False).mean()
        df['ema_slow'] = df['close'].ewm(span=self.slow, adjust=False).mean()
        df['macd'] = df['ema_fast'] - df['ema_slow']
        df['macd_signal'] = df['macd'].ewm(span=self.signal, adjust=False).mean()
        df['macd_hist'] = df['macd'] - df['macd_signal']
        return df
