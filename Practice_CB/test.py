"""
Sum two linked list.
Given two non-negative integers represented by linked lists, each node in the linked list stores a digit, and the digits are arranged in order from high to low.
For example, the linked list (2 -> 4 -> 3) represents the integer 243. You need to add the integers represented by
the two linked lists and return a linked list of the results in same order
1->2->1
1
-> 1-2-2
maximum length of each linked list: No limit
no trailing zero

6->5->0  : 0.65  length is n
3->4->1  : 0.341 length is m

m > n
-> m - n digit from one linkedlist first
->1.01


"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse(head) -> Node:
    if not head or not head.next:
        return head
    prev = ne = None
    while head:
        ne = prev
        prev = head
        head = head.next
        prev.next = ne
    return prev

class AddNumber:

    def get_length(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    def add_number_v2(self, head1, head2) -> Node:
        if not head1 or not head2:
            return head1 or head2
        n = self.get_length(head1)
        m = self.get_length(head2)
        if n > m:
            head1, head2 = head2, head1
            n, m = m, n

        head1 = self.reverse(head1)
        head2 = self.reverse(head2)


        dummy = tmp = Node(0)
        for _ in range(m - n):
            tmp.next = Node(head2.val)
            tmp = tmp.next
            head2 = self.get_next(head2)

        carry = 0
        while head1 or head2:
            carry += self.get_value(head1) + self.get_value(head2)
            tmp.next = Node(carry % 10)
            carry = carry // 10

            head1 = self.get_next(head1)
            head2 = self.get_next(head2)
            tmp = self.get_next(tmp)

        if carry > 0:
            tmp.next = Node(carry)
        else:
            tmp.next = Node(0)

        return self.reverse(dummy.next)

    def add_number(self, head1, head2) -> Node:
        if not head1 or not head2:
            return head1 or head2
        head1 = self.reverse(head1)
        head2 = self.reverse(head2)

        dummy = tmp = Node(0)
        carry = 0
        while head1 or head2:
            carry += self.get_value(head1) + self.get_value(head2)
            tmp.next = Node(carry % 10)
            carry = carry // 10

            head1 = self.get_next(head1)
            head2 = self.get_next(head2)
            tmp = self.get_next(tmp)

        if carry > 0:
            tmp.next = Node(carry)

        return self.reverse(dummy.next)

    def get_next(self, node) -> Node:
        if not node:
            return None
        return node.next

    def get_value(self, node) -> int:
        if not node:
            return 0
        return node.val

    def reverse(self, head) -> Node:
        if not head or not head.next:
            return head
        prev = ne = None
        while head:
            ne = prev
            prev = head
            head = head.next
            prev.next = ne
        return prev


def print_node(head):
    if not head:
        print("0")
        return
    ans = [""]
    while head:
        ans.append(str(head.val))
        head = head.next
    print("".join(ans))

def print_node_v2(head):
    if not head:
        print("0")
        return
    ans = []
    if head.val == 0:
        ans.append("0.")
    else:
        ans.append("1.")
    head = head.next

    while head:
        ans.append(str(head.val))
        head = head.next
    print("".join(ans))


def get_node_list(num: int) -> Node:
    dummy = tmp = Node(0)
    while num > 0:
        tmp.next = Node(num % 10)
        num = num // 10
        tmp = tmp.next
    return reverse(dummy.next)

def get_node_list_v2(num: int) -> Node:
    if num == 0:
        return Node(0)
    dummy = tmp = Node(0)
    while num > 0:
        tmp.next = Node(num % 10)
        num = num // 10
        tmp = tmp.next
    return reverse(dummy.next)

def test1():
    test_case = [(121, 1), (243, 100), (100, 0), (99, 1)]
    sol = AddNumber()
    for a, b in test_case:
        node_a = get_node_list(a)
        node_b = get_node_list(b)
        print_node(node_a)
        print_node(node_b)

        ans = sol.add_number(node_a, node_b)
        print_node(ans)
        print("-----------------------------")

def test2():
    # 0.65 + 0.341 = 0.991
    test_case = [(65, 341), (75, 751), (9, 1), (1, 0)]
    for a, b in test_case:
        sol = AddNumber()

        node_a = get_node_list_v2(a)
        node_b = get_node_list_v2(b)
       # print_node(node_a)
        #print_node(node_b)

        ans = ans = sol.add_number_v2(node_a, node_b)
        print_node_v2(ans)

test2()


