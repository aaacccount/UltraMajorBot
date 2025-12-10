class SignalFusion:
    def combine(self, mtf_data, structure_info):
        score = 0
        weights = {"15m":1, "1h":2, "4h":3, "1d":4, "1w":5}
        for tf, struct in structure_info.items():
            w = weights.get(tf, 1)
            if struct == "HH":
                score += w
            elif struct == "LL":
                score -= w
        if score >= 5:
            return "BUY"
        elif score <= -5:
            return "SELL"
        else:
            return "WAIT"
