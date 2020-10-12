from typing import List, Optional


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

    def __eq__(self, other):
        return list(map(lambda node: node.value, self)) == other

    def insert_into(self, position, value):
        """
        Insert a node into the exactly position in the linked list
        :param position: the position where the node will be inserted
        :param value: the value of the node
        """
        if self.head is None:
            raise Exception('The list is empty')

        previous_node = None
        current_position = 0

        for node in self:
            if current_position != position:
                previous_node = node
                current_position += 1
                continue

            new_node = Node(value, node.next_node)

            if current_position == 0:
                self.head = new_node
            else:
                previous_node.next_node = new_node

            return

        raise Exception("There's no such position in the list")

    def remove_from(self, position: int):
        """
        Remove node from given position
        :param position: the position of the node to be removed
        """
        if self.head is None:
            raise Exception('The list is empty')

        previous_node = None

        for node_position, node in enumerate(self):
            if node_position == position:
                if previous_node is None:
                    self.head = self.head.next_node

                else:
                    previous_node.next_node = node.next_node

                return

            previous_node = node

        raise Exception("There's no such position in the list")

    def reverse_itself_iteratively(self):
        """
        Reverse the linked list using iterative move
        """
        previous_node = None
        current_node = self.head

        while current_node is not None:
            future_current_node = current_node.next_node

            current_node.next_node = previous_node
            previous_node = current_node

            current_node = future_current_node

        self.head = previous_node

    def reverse_itself_recursively(self, head: Node) -> Optional[Node]:
        """
        Reverse the linked list using recursive mode
        """
        if head is None or head.next_node is None:
            return head

        new_head = self.reverse_itself_recursively(head.next_node)

        head.next_node.next_node = head
        head.next_node = None

        return new_head
