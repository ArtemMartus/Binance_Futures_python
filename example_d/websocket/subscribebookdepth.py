import logging
from binance_d import SubscriptionClient
from binance_d.constant.test import *
from binance_d.model import *
from binance_d.exception.binanceapiexception import BinanceApiException

from binance_d.base.printobject import *

logger = logging.getLogger("binance-futures")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

sub_client = SubscriptionClient(api_key=g_api_key, secret_key=g_secret_key)


def callback(data_type: 'SubscribeMessageType', event: 'any'):
    if data_type == SubscribeMessageType.RESPONSE:
        pass
    elif  data_type == SubscribeMessageType.PAYLOAD:
        PrintMix.print_data(event.bids)
        PrintMix.print_data(event.asks)



def error(e: 'BinanceApiException'):
    pass

sub_client.subscribe_book_depth_event("btcusd_200925", 10, callback, error, update_time=UpdateTime.FAST)
