# CryptoBot — simplified trading bot

This repo is a small CLI-based bot that places **market** and **limit** orders on Binance Futures Testnet.

Quick setup
1. Create a Python virtual environment and activate it
2. Install dependencies (e.g., `pip install python-dotenv python-binance pytest`)
3. Copy `.env` and set `BINANCE_API_KEY` and `BINANCE_API_SECRET` for testnet

Run
- `python main.py` — choose order type, symbol, side and quantity

Tests
- `pytest` will run unit tests (tests mock the Binance client so no real orders are placed)

Safety & notes
- This project is configured to target Binance Futures Testnet by default; still **use caution** and verify keys and mode before placing orders.
- Avoid committing `.env` or `bot.log` to version control.
- Consider adding input validation, dry-run, and risk controls before using more broadly.
