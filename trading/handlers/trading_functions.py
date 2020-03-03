class BestTrade:
    def buy_and_sell(self, rates):
        rate_list = rates
        list_rates = [{'day': 1, 'price': 10}, {'day': 2, 'price': 9}, {'day': 3, 'price': 4}, {'day': 4, 'price': 1},
                      {'day': 5, 'price': 6}]

        for i in range(len(list_rates)):
            entry = {'day': list_rates[i]['day'], 'price': list_rates[i]['price']}
            rate_list.append(entry)

        if len(rate_list) < 2:
            return 'The profit is Zero! No matches for a profit trade', 200

        prices = iter(rate_list)
        buy = next(prices, 0)
        profit = 0

        price_list = []
        for i in range(len(list_rates)):
            price_list.append(rate_list[i]['price'])

        profit = 0
        buy_price = price_list[0]

        for sell_price in price_list[1:]:
            profit = max(profit, sell_price - buy_price)
            buy_price = min(buy_price, sell_price)

        sell_day = rate_list[price_list.index(sell_price)]['day']
        buy_day = rate_list[price_list.index(buy_price)]['day']

        return sell_day, buy_day

