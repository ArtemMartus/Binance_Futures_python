import logging
from binance_f import RequestClient
from binance_f import SubscriptionClient
from binance_f.constant.test import *
from binance_f.model import *
from binance_f.exception.binanceapiexception import BinanceApiException

from binance_f.base.printobject import *

# Start user data stream
request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
listen_key = request_client.start_user_data_stream()

# Keep user data stream
result = request_client.keep_user_data_stream()

# Close user data stream
# result = request_client.close_user_data_stream()

logger = logging.getLogger("binance-client")
logger.setLevel(level=logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

sub_client = SubscriptionClient(api_key=g_api_key, secret_key=g_secret_key)


def callback(data_type: 'SubscribeMessageType', event: 'any'):
    if data_type == SubscribeMessageType.RESPONSE:
        pass
    elif  data_type == SubscribeMessageType.PAYLOAD:
        if(event.eventType == "ACCOUNT_UPDATE"):
            PrintMix.print_data(event.balances)
            PrintMix.print_data(event.positions)
        elif(event.eventType == "ORDER_TRADE_UPDATE"):
            if not event.activationPrice is None:
                pass
            if not event.callbackRate is None:
                pass
        elif(event.eventType == "listenKeyExpired"):
            pass



def error(e: 'BinanceApiException'):
    pass

sub_client.subscribe_user_data_event(listen_key, callback, error)
