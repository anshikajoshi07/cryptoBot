from binance.client import Client
from bot.logger import logger

class BinanceBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret, testnet=testnet)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
        logger.info("Binance Futures Testnet Client Initialized")
