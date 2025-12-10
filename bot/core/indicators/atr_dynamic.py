class ATRDynamic:
    def __init__(self, period=14, multiplier=1.5):
        self.period=period; self.multiplier=multiplier
    def calculate(self, df):
        df['high-low']=df['high']-df['low']
        df['high-close']=(df['high']-df['close'].shift()).abs()
        df['low-close']=(df['low']-df['close'].shift()).abs()
        df['tr']=df[['high-low','high-close','low-close']].max(axis=1)
        df['atr']=df['tr'].rolling(self.period).mean()
        df['atr_stop']=df['close']-df['atr']*self.multiplier
        return df
