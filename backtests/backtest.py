import pandas as pd

class Backtest:
    def __init__(self, strategy, data, initial_balance=1000, commission=0.0004):
        self.strategy = strategy
        self.data = data
        self.balance = initial_balance
        self.commission = commission
        self.trades = []

    def run(self):
        """
        Run backtest over all timeframes (simplified)
        """
        mtf_data = self.data
        structure_info = self.strategy.structure.detect(mtf_data)
        for i in range(len(mtf_data[self.strategy.settings.timeframes[0]])):
            signal = self.strategy.fusion.combine(mtf_data, structure_info)
            self._execute_trade(signal)

        self._report()

    def _execute_trade(self, signal):
        if signal == "BUY":
            self.trades.append(("BUY", self.balance))
        elif signal == "SELL":
            self.trades.append(("SELL", self.balance))

    def _report(self):
        total_trades = len(self.trades)
        buy_trades = len([t for t in self.trades if t[0] == "BUY"])
        sell_trades = len([t for t in self.trades if t[0] == "SELL"])
        print("📊 Backtest Report")
        print(f"Total trades: {total_trades}")
        print(f"BUY trades: {buy_trades}")
        print(f"SELL trades: {sell_trades}")
        print(f"Final balance: {self.balance}")
