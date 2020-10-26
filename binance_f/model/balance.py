class Balance:

    def __init__(self):
        self.asset = ""
        self.accountAlias = ""
        self.balance = ""
        self.withdrawAvailable = ""

    @staticmethod
    def json_parse(json_data):
        result = Balance()
        result.asset = json_data.get_string("asset")
        result.accountAlias = json_data.get_string("accountAlias")
        result.balance = json_data.get_string("balance")
        result.withdrawAvailable = json_data.get_string("withdrawAvailable")

        return result