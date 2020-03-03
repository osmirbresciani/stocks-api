from trading.handlers.routes_functions import StockViews

views = StockViews()

def configure_routes(app):
    @app.route('/')
    def first_page():
        return views.start()

    @app.route('/list_rates', methods=['GET'])
    def list_rates():
        return views.get_rates(views.rates)

    @app.route('/send_rates', methods=['POST'])
    def rates():
        return views.send_rates()

    @app.route('/trade', methods=['GET'])
    def trade():
        return views.get_trade()
