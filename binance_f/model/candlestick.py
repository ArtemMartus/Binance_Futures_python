class Candlestick:

    def __init__(self):
        self.openTime = ""
        self.open = ""
        self.high = ""
        self.low = ""
        self.close = ""
        self.volume = ""
        self.closeTime = ""
        self.quoteAssetVolume = ""
        self.numTrades = ""
        self.takerBuyBaseAssetVolume = ""
        self.takerBuyQuoteAssetVolume = ""
        self.ignore = ""

    @staticmethod
    def json_parse(json_data):
        result = Candlestick()
        val = json_data.convert_2_list()
        result.openTime = val[0]
        result.open = val[1]
        result.high = val[2]
        result.low = val[3]
        result.close = val[4]
        result.volume = val[5]
        result.closeTime = val[6]
        result.quoteAssetVolume = val[7]
        result.numTrades = val[8]
        result.takerBuyBaseAssetVolume = val[9]
        result.takerBuyQuoteAssetVolume = val[10]
        result.ignore = val[11]
  
        return result