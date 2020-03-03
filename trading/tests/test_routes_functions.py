from trading.handlers.routes_functions import StockViews

views = StockViews()


def test_start():
    assert 'Stocks-Trading API' == views.start()


def test_start_empty_error():
    assert '' != views.start()


def test_get_trade():
    rates1 = [
        {
            "day": 1,
            "price": 2
        },
        {
            "day": 2,
            "price": 8
        }

    ]
    result = views.get_trade(rates1)
    assert result != None
    assert result[0] == 6
