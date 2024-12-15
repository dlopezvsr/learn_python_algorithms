# The purpose of this exercise is to swap two items in the list: item2 and item5.
# Remember the following:
# - You have to keep track of the node that contains the data entered: node_a such as node_b
# - You have to keep track of the previous node for each node matched with the data, I mean, node_a's previous node and
#   node_b's previous node. This will be useful later when we swap the elements to update the links properly.
# Then you have to also swap the node_b's next node for node_a's next node and vice versa.
# Lastly, you have to validate that either node_b or node_a previous has the value entered, otherwise - infinite loop.
# Validate that the two values are different also if so the nodes don't need to be changed.

from linked_lists import LinkedList


class NodeSwap:
    def __init__(self, ll):
        self.ll = ll

    def swap_elements(self, value1, value2):
        node_a = self.ll.head
        node_b = self.ll.head
        prev_node_a = ""
        prev_node_b = ""

        while node_a:
            if node_a.value == value1 or node_a.value is None:
                break
            node_a = node_a.next_node
            prev_node_a = node_a

        while node_b:
            if node_b.value == value2 or node_b.value is None:
                break
            node_b = node_b.next_node
            prev_node_b = node_b

        if node_a is None or node_b is None:
            print("Values not found")
            return

        if prev_node_a is None:
            self.head = node_b
        else:
            prev_node_a.set_next_node(node_b)

        if prev_node_b is None:
            self.head = node_a
        else:
            prev_node_b.set_next_node(node_a)

        node_a.set_next_node(node_b.next_node)
        node_b.set_next_node(node_a.next_node)


node1 = LinkedList(1)

for i in range(1, 7):
    node1.insert_head_node(i)


list_to_swap = NodeSwap(node1)
list_to_swap.swap_elements(2, 5)
