from bot.core.indicators.macd import MACD
from bot.core.indicators.vwap import VWAP
from bot.core.indicators.atr_dynamic import ATRDynamic
from bot.core.indicators.ob_fvg import OrderBlocks, FairValueGap
from bot.core.indicators.divergence import Divergence

class ConfidenceScorer:
    def __init__(self):
        self.macd = MACD()
        self.vwap = VWAP()
        self.atr = ATRDynamic()
        self.ob = OrderBlocks()
        self.fvg = FairValueGap()
        self.div = Divergence()

    def score(self, df):
        """
        Returns a confidence score 0-100
        based on indicators
        """
        score = 50  # base 50

        # MACD
        macd_df = self.macd.calculate(df)
        if macd_df['macd'].iloc[-1] > macd_df['macd_signal'].iloc[-1]:
            score += 10
        else:
            score -= 10

        # VWAP
        vwap_df = self.vwap.calculate(df)
        if df['close'].iloc[-1] > vwap_df['vwap'].iloc[-1]:
            score += 5
        else:
            score -= 5

        # ATR Dynamic
        atr_df = self.atr.calculate(df)
        if df['close'].iloc[-1] > atr_df['atr_stop'].iloc[-1]:
            score += 5
        else:
            score -= 5

        # OB & FVG & Divergence placeholders
        # These can add/subtract 5-10 points each when implemented

        score = max(0, min(100, score))
        return score
