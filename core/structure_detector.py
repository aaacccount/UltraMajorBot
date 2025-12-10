class StructureDetector:

    def detect(self, mtf_data):
        """
        Detects basic market structure (HH / LL / RANGE) for each timeframe
        """
        result = {}
        for tf, df in mtf_data.items():
            highs = df["high"]
            lows = df["low"]

            if highs.iloc[-1] > highs.iloc[-5]:
                structure = "HH"
            elif lows.iloc[-1] < lows.iloc[-5]:
                structure = "LL"
            else:
                structure = "RANGE"

            result[tf] = structure
        return result
