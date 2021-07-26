"""
This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. Instead of each node
holding next and prev fields, it holds a field named both, which is an XOR of the next
node and the previous node. Implement an XOR linked list; it has an add(element) which
adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have
access to get_pointer and dereference_pointer functions that converts between nodes
and memory addresses.

"""
# https://github.com/subsr97/daily-coding-problem/blob/master/challenges/xor-linked-list.py

#TODO : unsolved
import ctypes

# https://www.geeksforgeeks.org/xor-linked-list-a-memory-efficient-doubly-linked-list-set-2/
class XORNode(object):
    def __init__(self, data):
        self.data = data
        self.xor_addr = None

    def __repr__(self):
        return f"XORNode({self.data}, {self.xor_addr})"


class XORList(object):
    def __init__(self, head: XORNode = None):
        self.head = head

    def add(self, new_node):
        """
        Add data to the end of the list
        :param data:
        :return:
        """
        print("*"*100)
        print(self.head)
        # new_node = XORNode(data=data)
        # new_node.xor_addr = 0
        print(f"Adding new {new_node} with mem_id: {id(new_node)} and with data: {new_node.data}")

        if self.head is None:
            self.head = new_node
        else:
            print("\nIterating the list from head...")

            prev_ptr_id = 0
            node = self.head
            next_ptr_id = None if node.xor_addr == None else node.xor_addr ^ prev_ptr_id

            print(f"prev_ptr_id: {prev_ptr_id} node: {node} next_ptr_id: {next_ptr_id} node_mem_id: {id(node)}")

            while self.cast(next_ptr_id):
                # get next node
                print("while")
                node_mem_id = node.xor_addr ^ id(prev_ptr_id)
                print(node_mem_id)
                node = self.cast(node_mem_id)
                prev_ptr_id = next_ptr_id
                next_ptr_id = id(node)
                print(f"prev_ptr_id: {prev_ptr_id} node: {node} next_ptr_id: {next_ptr_id} node_mem_id: {id(node)}")

            print("inserting the new node:")
            # next pointer of current node
            node.xor_addr = node.xor_addr ^ id(new_node)
            # previous pointer of new node
            new_node.xor_addr = new_node.xor_addr ^ id(node)
            print(node)
            print(new_node)
            print("done")
        print(self.head)


    # def get(self, index):
    #     print("\n\nget")
    #     i = 0
    #
    #     print("Iterating the list...")
    #
    #     prev_ptr_id = 0
    #     node = self.head
    #     print(node)
    #     next_ptr_id = None if node.xor_addr == None else self.next_id(xor_addr=node.xor_addr, prev_addr_id=prev_ptr_id)
    #
    #     print(f"prev_ptr_id: {prev_ptr_id} node: {node} next_ptr_id: {next_ptr_id} node_id: {id(node)}")
    #     print(self.cast(next_ptr_id))
    #     while self.cast(next_ptr_id) and i != index:
    #         print("while")
    #         node = self.cast(self.XOR(node.xor_addr, id(prev_ptr_id)))
    #         prev_ptr_id = next_ptr_id
    #         next_ptr_id = id(node)
    #         i += 1
    #
    #     return node.data

    def cast(self, mem_id):
        print(f"casting {mem_id} {type(mem_id)}")
        if mem_id is None or mem_id == 0:
            return None
        else:
            return ctypes.cast(mem_id, ctypes.py_object).value


if __name__ == '__main__':

    # n = XORNode(data=1)
    # print(n)
    # print(id(n))
    # print(ctypes.cast(id(n), ctypes.py_object).value)

    l = XORList()
    new_node = XORNode(data=1)
    new_node.xor_addr = 0
    l.add(new_node)
    new_node = XORNode(data=2)
    new_node.xor_addr = 0
    l.add(new_node)
    new_node = XORNode(data=3)
    new_node.xor_addr = 0
    l.add(new_node)
    # l.add(4)
    pass

    # print("Finally got: ", l.get(1))

