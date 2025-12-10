import pandas as pd

class VWAP:
    def calculate(self, df):
        q = df['volume']
        p = df['close']
        df['vwap'] = (p * q).cumsum() / q.cumsum()
        return df
