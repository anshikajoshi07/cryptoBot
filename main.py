import os
from dotenv import load_dotenv
from bot.binance_bot import BinanceBot
from bot.orders import place_market_order, place_limit_order

load_dotenv()

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

bot = BinanceBot(api_key, api_secret)

print("1. Market Order")
print("2. Limit Order")

choice = input("Choose order type: ")
symbol = input("Symbol (e.g. BTCUSDT): ")
side = input("Side (BUY / SELL): ")
quantity = float(input("Quantity: "))

if choice == "1":
    place_market_order(bot.client, symbol, side, quantity)

elif choice == "2":
    price = input("Price: ")
    place_limit_order(bot.client, symbol, side, quantity, price)

else:
    print("Invalid choice")
