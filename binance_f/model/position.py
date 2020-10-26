class Position:

    def __init__(self):
        self.entryPrice = ""
        self.isAutoAddMargin = False
        self.leverage = ""
        self.maxNotionalValue = ""
        self.liquidationPrice = ""
        self.markPrice = ""
        self.positionAmt = ""
        self.symbol = ""
        self.unrealizedProfit = ""
        self.marginType = ""
        self.isolatedMargin = ""
        self.positionSide = ""


    @staticmethod
    def json_parse(json_data):
        result = Position()
        result.entryPrice = json_data.get_string("entryPrice")
        result.isAutoAddMargin = json_data.get_boolean("isAutoAddMargin")
        result.leverage = json_data.get_string("leverage")
        result.maxNotionalValue = json_data.get_string("maxNotionalValue")
        result.liquidationPrice = json_data.get_string("liquidationPrice")
        result.markPrice = json_data.get_string("markPrice")
        result.positionAmt = json_data.get_string("positionAmt")
        result.symbol = json_data.get_string("symbol")
        result.unrealizedProfit = json_data.get_string("unRealizedProfit")
        result.marginType = json_data.get_string("marginType")
        result.isolatedMargin = json_data.get_string("isolatedMargin")
        result.positionSide = json_data.get_string("positionSide")
        return result
