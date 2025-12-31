from bot.logger import logger

def place_market_order(client, symbol, side, quantity):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )
        logger.info(f"Market Order Placed: {order}")
        return order
    except Exception as e:
        logger.error(f"Market Order Error: {e}")
        return None


def place_limit_order(client, symbol, side, quantity, price):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )
        logger.info(f"Limit Order Placed: {order}")
        return order
    except Exception as e:
        logger.error(f"Limit Order Error: {e}")
        return None
