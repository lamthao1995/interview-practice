import collections
import heapq
from typing import *
class InvalidInputException(Exception):
    pass


class Transaction:
    def __init__(self, id: int, fee: int, size: int):
        self.id = id
        self.fee = 1.0 * fee
        self.size = size
    def __repr__(self):
        return "id = %s" % (self.id,)
class MaximizeTransaction:
    def get_optimal_transactions(self, transactions: List[Transaction], block_sz: int) -> List[Transaction]:
        if not transactions:
            return []
        ans = []
        transactions.sort(key=lambda x: 1.0 * x.fee / x.size)
        total_size = 0
        for tx in transactions:
            if total_size > block_sz:
                break
            if total_size + tx.size <= block_sz:
                total_size += tx.size
                ans.append(tx)
        return ans

    def toposort(self, dependencies: List[List[int]], map_fee_ratio: dict) -> List[int]:
        """
        :param dependencies: list of edges: a -> b
        :return: List of ids in topo sort
        """
        unique_set = set()
        gr = collections.defaultdict(list)
        in_degree_counter = collections.defaultdict(lambda : 0)
        for a, b in dependencies:
            unique_set.update([a, b])
            gr[a].append(b)
            in_degree_counter[b] += 1

        pool = []
        for node in unique_set:
            if in_degree_counter[node] == 0:
                pool.append((-map_fee_ratio[node], node))
        heapq.heapify(pool)
        ans = []
        while pool:
            _, cur = heapq.heappop(pool)
            ans.append(cur)
            for ne in gr[cur]:
                in_degree_counter[ne] -= 1
                if in_degree_counter[ne] == 0:
                    heapq.heappush(pool, (-map_fee_ratio[ne], ne))

        if len(ans) != len(unique_set):
            raise InvalidInputException("contains cycle")
        return ans

def get_transaction_list_with_dependency(self, tx_list, dependency_list, block_sz) -> List[Transaction]:
    map_fee_ratio = {node.id: node.fee / node.size for node in tx_list}
    topo_tx_list = self.toposort(dependency_list, map_fee_ratio)
    ans = []
    total_size = 0
    for tx in topo_tx_list:
        if total_size > block_sz:
            break
        if total_size + tx.size <= block_sz:
            total_size += tx.size
            ans.append(tx)
    return ans

def get_transaction_list(tx_list: List[tuple]) -> List[Transaction]:
    ans = []
    for i, fee, sz in tx_list:
        ans.append(Transaction(i, fee, sz))
    return ans

def test():
    tests = []
    tests.append(([(1, 10, 2),
    (2, 20, 3),
    (3, 15, 5),
    (4, 26, 7)], 9))
    sol = MaximizeTransaction()
    for t_list, bz in tests:
        transactions = get_transaction_list(t_list)
        ans = sol.get_optimal_transactions(transactions, bz)
        total = 0
        for t in ans:
            total += t.fee
        print("total fee: ", total, " and with tx = ", ans)
test()