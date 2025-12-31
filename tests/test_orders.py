import pytest
from types import SimpleNamespace

from bot.orders import place_market_order, place_limit_order


class FakeClient:
    def __init__(self, to_return=None, to_raise=None):
        self._to_return = to_return
        self._to_raise = to_raise
        self.last_call = None

    def futures_create_order(self, **kwargs):
        self.last_call = kwargs
        if self._to_raise:
            raise self._to_raise
        return self._to_return


def test_place_market_order_success():
    fake_resp = {"orderId": 123}
    client = FakeClient(to_return=fake_resp)

    result = place_market_order(client, symbol="BTCUSDT", side="BUY", quantity=0.01)

    assert result == fake_resp
    assert client.last_call["type"] == "MARKET"
    assert client.last_call["symbol"] == "BTCUSDT"


def test_place_market_order_exception():
    client = FakeClient(to_raise=Exception("fail"))

    result = place_market_order(client, symbol="BTCUSDT", side="SELL", quantity=0.02)

    assert result is None


def test_place_limit_order_success():
    fake_resp = {"orderId": 456}
    client = FakeClient(to_return=fake_resp)

    result = place_limit_order(client, symbol="BTCUSDT", side="BUY", quantity=0.01, price="50000")

    assert result == fake_resp
    assert client.last_call["type"] == "LIMIT"
    assert client.last_call["price"] == "50000"
    assert client.last_call["timeInForce"] == "GTC"


def test_place_limit_order_exception():
    client = FakeClient(to_raise=RuntimeError("oops"))

    result = place_limit_order(client, symbol="BTCUSDT", side="SELL", quantity=0.05, price="60000")

    assert result is None
