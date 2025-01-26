from typing import *
class Transaction:
    def __init__(self, id: int, user_id: int, currency: str, amount: float, time_ts: int):
        self.id = id
        self.user_id = user_id
        self.currency = currency
        self.amount = amount
        self.time_ts = time_ts

    def __repr__(self):
        return "id = %s" % (self.id, )

class QueryTransaction:
    def __init__(self, transaction_list):
        self.transaction_list = list(transaction_list)
        self.filter_dict = {}

    def filter_with_time(self, from_time: int, to_time: int) -> "QueryTransaction":
        if from_time is not None:
            self.filter_dict["from_time"] = from_time
        if to_time is not None:
            self.filter_dict["to_time"] = to_time

        return self

    def filter_with_currency(self, currency: str) -> "QueryTransaction":
        self.filter_dict["currency"] = currency.lower()
        return self

    def build_list(self, last_id=0, count=None) -> List[Transaction]:
        ans = []
        for tx in self.transaction_list:
            if self._is_valid(tx, last_id):
                ans.append(tx)
            if count is not None and len(ans) == count:
                break
        return ans

    def _is_valid(self, tx: Transaction, last_id=None):
        if "from_time" in self.filter_dict and tx.time_ts < self.filter_dict["from_time"]:
            return False
        if "to_time" in self.filter_dict and tx.time_ts > self.filter_dict["to_time"]:
            return False
        if "currency" in self.filter_dict and self.filter_dict["currency"] != tx.currency:
            return False
        if last_id is not None and tx.id <= last_id:
            return False

        return True


def test():
    test_cases = []
    test_one = [
        Transaction(1, 2, "sgd", 100, 10),
        Transaction(2, 3, "sgd", 200, 20),
        Transaction(3, 4, "usd", 300, 15)
    ]
    test_cases.append(test_one)
    for tx_list in test_cases:
        sol = QueryTransaction(tx_list)
        ans = sol.filter_with_time(10, 20).filter_with_currency("sgd").build_list(1, 1)
        print(ans)
test()