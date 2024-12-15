class Node:
    """
    A node will store data and a link to the next node. Under node class you can create methods to retrieve
    data stored and also the next node. Another important method is the ´set_next_node´ which will be used to assign
    links to next node.
    """

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_value(self):
        return self.value


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def insert_beginning(self, value):
        self.head = Node(value, self.head)

    def insert_tail_node(self, value):
        self.head.next_node = Node(value)

    def stringify_list(self):
        current_node = self.head
        list_of_nodes = ""
        while current_node:
            list_of_nodes = list_of_nodes + "\n" + str(current_node.value)
            current_node = current_node.next_node
        return list_of_nodes
