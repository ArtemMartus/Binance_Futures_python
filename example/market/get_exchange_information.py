from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
result = request_client.get_exchange_information()
PrintMix.print_data(result.rateLimits)
PrintMix.print_data(result.exchangeFilters)
PrintMix.print_data(result.symbols)
