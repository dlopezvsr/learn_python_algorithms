class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Initialize next as null


class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list as None

    def append(self, data):
        new_node = Node(data)  # Create a new node
        if self.head is None:
            self.head = new_node  # If the list is empty, set the new node as the head
            return
        last_node = self.head
        while last_node.next:  # Traverse to the last node
            last_node = last_node.next
        last_node.next = new_node  # Append the new node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" -> ")
            cur_node = cur_node.next
        print("None")

    def delete_node(self, key):
        cur_node = self.head

        # If the node to be deleted is the head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            return

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        # If the key is not present in the linked list
        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None


# Example usage
if __name__ == "__main__":
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(4)
    llist.delete_node(3)
    llist.append(5)

    print("Original list:")
    llist.print_list()

    # llist.delete_node(3)
    # print("List after deleting 3:")
    # llist.print_list()
