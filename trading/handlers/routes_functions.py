from flask import jsonify, request
from trading.data.database_functions import *


class StockViews:
    def __init__(self):
        self.rates = []

    def start(self):
        return 'Stocks-Trading API'

    def send_rates(self):
        create_table()
        input = request.get_json()
        insert_rates(input)
        return jsonify(input), 201

    def get_rates(self, rates):
        return jsonify(rates), 200

    def get_trade(self):
        try:
            rate_list = get_rates()
            arr = [x for xs in rate_list for x in xs]
            rates_data = []
            for i in range(len(arr)):
                data = {'day': i + 1, 'price': float(arr[i])}
                rates_data.append(data)

            if len(rates_data) < 2:
                return 'The profit is Zero! No matches for a profit trade.', 200

            prices = iter(rates_data)
            buy = next(prices, 0)
            profit = 0

            price_list = []
            for i in range(len(rates_data)):
                price_list.append(rates_data[i]['price'])

            sell_price = 0
            profit = 0
            buy_price = price_list[0]

            for sell_price in price_list[1:]:
                profit = max(profit, sell_price - buy_price)
                buy_price = min(buy_price, sell_price)

            sell_day = rates_data[price_list.index(sell_price)]['day']
            buy_day = rates_data[price_list.index(buy_price)]['day']

            trade = [
                {
                    'profit': profit,

                    'buy':
                        {
                            'day': buy_day,
                            'price': buy_price,

                            'sell':
                                {
                                    'day': sell_day,
                                    'price': sell_price
                                },
                        }
                }

            ]

            return jsonify(trade), 200
        except Exception:
            return r"Error! Rate's list is empty", 404

