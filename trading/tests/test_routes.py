from flask import Flask
import json

from trading.handlers.routes import configure_routes


def init():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    return client


def test_first_page():
    client = init()
    url = '/'

    response = client.get(url)
    assert response.get_data() == b'Stocks-Trading API'
    assert response.status_code == 200


def test_list_rates():
    client = init()
    url = '/list_rates'

    response = client.get(url)
    assert response.status_code == 200


def test_send_rates():
    client = init()
    url = '/send_rates'

    input = [{
        'day': '1',
        'price': '5'
    }]

    response = client.post(url, data=json.dumps(input))
    assert response.status_code == 201


def test_trade_empty_error():
    client = init()
    url = '/trade'

    response = client.get(url)
    assert response.status_code == 404

    msg_error = r"Error! Rate's List is empty"
    assert response.get_data() == b'%s' % msg_error.encode("utf-8")

def test_trade_():
    client = init()
    url = '/trade'

    response = client.get(url)
    assert response.status_code == 200


