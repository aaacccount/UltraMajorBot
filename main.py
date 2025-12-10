from bot.strategies.MTFStrategy.mtf_strategy import MTFStrategy
from bot.config.settings import Settings

def main():
    print("🚀 Ultra-Major Bot Start")
    settings = Settings()
    strategy = MTFStrategy(settings=settings)
    strategy.run_live_loop()

if __name__ == "__main__":
    main()
