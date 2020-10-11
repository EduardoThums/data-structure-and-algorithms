from unittest import TestCase

from linked_list.linked_list_impl import LinkedList


class TestLinkedList(TestCase):

    def test_remove_node_from_beginning_list_should_succeed(self):
        linked_list = LinkedList([1, 2, 3])
        linked_list.remove_from(0)

        expected_list = [2, 3]

        self.assertEqual(expected_list, linked_list)

    def test_remove_node_from_the_end_of_the_list_should_succeed(self):
        linked_list = LinkedList([1, 2, 3])
        linked_list.remove_from(2)

        expected_list = [1, 2]

        self.assertEqual(expected_list, linked_list)

    def test_remove_node_from_the_middle_of_the_list_should_succeed(self):
        linked_list = LinkedList([1, 2, 3])
        linked_list.remove_from(1)

        expected_list = [1, 3]

        self.assertEqual(expected_list, linked_list)
