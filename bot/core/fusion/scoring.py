from bot.core.indicators.macd import MACD
from bot.core.indicators.vwap import VWAP
from bot.core.indicators.atr_dynamic import ATRDynamic

class ConfidenceScorer:
    def __init__(self):
        self.macd=MACD(); self.vwap=VWAP(); self.atr=ATRDynamic()
    def score(self, df):
        score=50
        macd_df=self.macd.calculate(df)
        if macd_df['macd'].iloc[-1]>macd_df['macd_signal'].iloc[-1]: score+=10
        else: score-=10
        vwap_df=self.vwap.calculate(df)
        if df['close'].iloc[-1]>vwap_df['vwap'].iloc[-1]: score+=5
        else: score-=5
        atr_df=self.atr.calculate(df)
        if df['close'].iloc[-1]>atr_df['atr_stop'].iloc[-1]: score+=5
        else: score-=5
        return max(0,min(100,score))
