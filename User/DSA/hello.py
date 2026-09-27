class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)
    def __repr__(self):
        return str(self.data)


def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.data)
        current = current.next
    return result

if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    # Convert linked list to list
    result_list = linked_list_to_list(head)
    print(result_list)  # Output: [1, 2, 3] 