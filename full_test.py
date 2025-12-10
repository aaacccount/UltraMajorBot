from bot.config.settings import Settings
from bot.strategies.MTFStrategy.mtf_strategy import MTFStrategy
from bot.backtests.backtest import Backtest
from bot.core.timeframe_engine import TimeframeEngine

def run_full_test():
    print("🚀 Ultra-Major Bot Full Test Start")
    settings = Settings()
    strategy = MTFStrategy(settings=settings)
    engine = TimeframeEngine(settings)
    mtf_data = engine.fetch_multi_timeframe()
    backtester = Backtest(strategy=strategy,data=mtf_data,
                          initial_balance=settings.initial_balance,
                          commission=settings.commission)
    backtester.run()
    print("🔥 Live loop demo (3 cycles)")
    for _ in range(3):
        structure_info=strategy.structure.detect(mtf_data)
        signal=strategy.fusion.combine(mtf_data,structure_info)
        print("🔎 Live Signal →",signal)

if __name__=="__main__":
    run_full_test()
