from typing import List


class Node:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        return str(self.value)


class LinkedList:

    def __init__(self, values: List[int]):
        self.head = None

        if values:
            self.head = Node(values.pop(0))
            current_node = self.head

            for value in values:
                new_node = Node(value)
                current_node.next_node = new_node
                current_node = new_node

    def __repr__(self):
        current_node = self.head
        nodes = []

        while current_node is not None:
            nodes.append(str(current_node))
            current_node = current_node.next_node

        nodes.append('None')
        return ' -> '.join(nodes)

    def __iter__(self):
        current_node = self.head

        while current_node is not None:
            yield current_node
            current_node = current_node.next_node

    def _insert_into(self, position, value):
        """
        Insert a node into the exactly position in the linked list
        :param position: the position where the node will be inserted
        :param value: the value of the node
        """


if __name__ == '__main__':
    linked_list = LinkedList([1,2,4,5,6])

    print(linked_list)

    for node in linked_list:
        print(node)
