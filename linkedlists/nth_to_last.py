from linked_lists import LinkedList


# Complete this function:
def nth_last_node(linked_list, n):
    nth_last_node = None
    tail_node = linked_list.head
    counter = 1
    while tail_node:
        counter += 1
        tail_node = tail_node.get_next_node()

        if counter >= n + 1:
            if nth_last_node is None:
                nth_last_node = linked_list.head
            else:
                nth_last_node = nth_last_node.get_next_node()
    return nth_last_node


def generate_test_linked_list_0():
    linked_list = LinkedList(50)
    for i in range(49, 0, -1):
        linked_list.insert_beginning(i)
    return linked_list


# Use this to test your code:
test_list = generate_test_linked_list_0()
print(test_list.stringify_list())
nth_last = nth_last_node(test_list, 9)
print(f"This is the nth to last node: {nth_last.value}")


def find_middle(linked_list):
    fast_pointer = linked_list.head
    slow_pointer = linked_list.head

    while fast_pointer is not None:
        fast_pointer = fast_pointer.get_next_node()
        if fast_pointer is not None:
            fast_pointer = fast_pointer.get_next_node()
            slow_pointer = slow_pointer.get_next_node()

    return slow_pointer






def generate_test_linked_list_1(length):
    linked_list = LinkedList(length)
    for i in range(length - 1, 0, -1):
        linked_list.insert_beginning(i)
    return linked_list


# Use this to test your code:
test_list = generate_test_linked_list_1(7)
print(test_list.stringify_list())
middle_node = find_middle(test_list)
print(middle_node.value)
