class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def create_linked_list(arr):
    if not arr:
        return None

    head = Node(arr[0])      # Create head
    current = head           # Pointer to traverse the list

    for value in arr[1:]:
        current.next = Node(value)
        current = current.next

    return head


def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


if __name__ == "__main__":
    arr = [2, 5, 8, 7]

    head = create_linked_list(arr)

    print_linked_list(head)


//method easy
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


if __name__ == "__main__":

    arr = [2, 5, 8, 7]

    y = Node(arr[0])      # head node
    temp = y              # pointer to build the list

    for i in range(1, len(arr)):
        temp.next = Node(arr[i])
        temp = temp.next

    # print linked list
    curr = y
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")
