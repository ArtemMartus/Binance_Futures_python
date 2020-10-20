from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
result = request_client.get_order_book(symbol = "BTCUSDT", limit = 10)
PrintMix.print_data(result.bids)
PrintMix.print_data(result.asks)