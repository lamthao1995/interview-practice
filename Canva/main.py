"""
input: 
{
  "pizza" : ["dough", "tomato"], -> m = 3 items, maximum length of items  n= 6 (characters)
  "dough": [],
  "tomato": []
}
output: ["tomato", "dough", "pizza"] or ["dough", "tomato", "pizza"]

input: dictionary: contains key: name of food, value: list of ingredient
output: return list of food in order 
always have valid answer

Step1: build a graph -> DAG
Step 2: start with nodes with in-degree = 0 -> use BFS -> generate answer
        1 -> 2->3
            0->3
        1 -> 2 -> 3
        1-> 4
        
        t = 0 -> start at node 1 
        t = 1 -> come to 2 nodes: 2, 4
        t = 2 -> come to node 3
        -> ans = [1, 2, 4, 3]
"""
from typing import *
import collections

class InvalidException(Exception):
    pass

class ItemNode:
    def __init__(self, name):
        self.name_item = name
        self.children = []
    def add_node(self, node):
        self.children.append(node)

class GetListIngredient:
    def __init__(self):
        pass

    def get_list_of_ingredient(self, gr: dict) -> List[str]:
        """
        item: string
        assume: max length of item: n , if length of item is constant
        we have m items -> time complexity: O(m + x), Space: O(m + x)
        say x: number of edges
        for dict, set: we have at most m items
        :param gr:
        :return:
        """
        if not gr:
            return []
        graph_dict = collections.defaultdict(list)
        counter = {} # in-degree counter
        unique_node = set()

        #1st step: build DAG with input
        for k, value_list in gr.items():
            unique_node.add(k)
            for ne in value_list:
                counter[k] = counter.get(k, 0) + 1
                unique_node.add(ne)
                graph_dict[ne].append(k)

        #print(graph_dict)
        # 2nd step: start with nodes (their in-degree = 0)
        pool = collections.deque()
        ans = []
        for item in unique_node:
            if counter.get(item, 0) == 0:
                pool.append(item)
                ans.append(item)
       # print(counter, pool)

        #3rd step: use BFS -> we can come to next node if counter[next_node] == 0
        used_set = set(pool)
        while pool:
            for _ in range(len(pool)):
                cur_item = pool.popleft()
                for next_item in graph_dict.get(cur_item, []):
                    counter[next_item] = counter.get(next_item, 0) - 1
                    if next_item in used_set:
                        continue
                    if counter.get(next_item, 0) != 0:
                        continue
                    ans.append(next_item)
                    used_set.add(next_item)
                    pool.append(next_item)
        if len(ans) != len(unique_node):
            raise InvalidException("contain cycle")

        return ans

def test():
    tests = []
    tests.append({
        "pizza" : ["dough", "tomato"],
        "dough": [],
        "tomato": []
    })
    tests.append({
        "pizza": ["dough", "tomato"],
    })
    tests.append({
      "flour" : [],
      "dough" : ["flour"],
      "pizza" : ["dough"]
    })

    tests.append({
        "flour": ["dough"],
        "dough": ["flour"],
    })

    tests.append({
      "pizza" : ["dough", "tomato"],
      "dough": ["flour", "water"],
      "tomato": [],
      "water": [],
      "flour": []
    })

    sol = GetListIngredient()
    for gr in tests:
        try:
            ans = sol.get_list_of_ingredient(gr)
            print(ans)
        except Exception as ex:
            print("invalid input because of ex=: ", ex, " and input = ", gr)
test()


