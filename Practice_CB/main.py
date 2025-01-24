"""
Input string "{'key':'value'}"
key: string
value: string
output map['key']

key, value contains no ,

example: "{'lam': 'microsoft'}" -> {'lam': 'microsoft'}
{k1: {...}, k2: {} }
SET_OF_INVALID_KEY_VALUE_CHAR = "{},:"
"lam": "mai", "key":{"k": "v"} => new layer: "k": "v"
func parse_dict(s, idx):
    temp_list = []
    while idx < len(s) and s[idx] != "}":
        if s[idx] == "{":
            next_idx, next_dict = parse_dict(s, idx + 1)
            idx = next_id
            temp_list.append(next_dict)
        else if s[idx] == "," or s[idx] == " " or s[idx] == ":":
            idx += 1
        else:
            value = ""
            while idx < len(s) and s[idx] not in SET_OF_INVALID_KEY_VALUE_CHAR:
                value += s[idx]
                idx += 1
            temp_list.append(value)
        ....
    for idx in range(0, len(temp_list, 2):
        cur_dict[temp_list[idx]] = temp_list[idx + 1]
    return idx + 1, cur_dict

"""
QUOTE = "'"
OPEN_PARENTHESIS = "{"
CLOSE_PARENTHESIS = "}"
class ParseDictionary:
    def parse_string_to_dict(self, s: str) -> dict:
        # time complexity: O(n), Space complexity: O(n) (n is length of input)
        if not s:
            return {}

        try:
            return self._parse_string_to_dict(s)
        except Exception as ex:
            print("failed to parse dict with value = ", s, " and ex = ", ex)
            return {}

    def _parse_string_to_dict(self, s: str) -> dict:
        s = s.strip()
        n = len(s)
        if s[0] !=OPEN_PARENTHESIS or s[-1] != CLOSE_PARENTHESIS:
            raise Exception("it is not a dict: value = ", s)
        s = s[1: n - 1]

        key_value_list = s.split(",")
        ans_dict = {}

        for val in key_value_list:
            key, value = val.split(":")
            key = self._remove_quote(key)
            value = self._remove_quote(value)

            ans_dict[key] = value
        return ans_dict

    def _remove_quote(self, value: str) -> str:
        value = value.strip()
        n = len(value)
        if value[0] != QUOTE or value[-1] != QUOTE:
            raise Exception("value is not correct format: value = ", value)
        return value[1: n - 1]

def test():
    sol = ParseDictionary()
    test_cases = ["", "{", "}", "", "{'lam': 'microsoft'}", "{'key':'value'}", "{'key':'value',}", "{'key':'value', key: value}", "{'key':value}"]
    test_cases.extend(["{'key' 'value'}"])
    for t in test_cases:
        print(sol.parse_string_to_dict(t))

#test()


"""
problem 2: 

"""
class Item:
    def __init__(self, value: str):
        self.value = value  # No.1
        self.lock = Lock()
        self.is_out_of_stock = False

    def buy(self):
        self.lock.acquire(time_out=1)
        self.is_out_of_stock = True
        self.lock.release()


    def can_buy(self):
        return self.is_out_of_stock == False

class Seller:
    def __init__(self):
        self.item_list = {} #key: name of item, value: ...

    def add_item(self, item: Item):
        pass

    def serve_request(self, url):
        pass

