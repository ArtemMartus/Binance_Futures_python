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
        PrintBasic.print_obj(event.data)
        sub_client.unsubscribe_all()


def error(e: 'BinanceApiException'):
    pass

sub_client.subscribe_index_candlestick_event("btcusd", CandlestickInterval.MIN1, callback, error)