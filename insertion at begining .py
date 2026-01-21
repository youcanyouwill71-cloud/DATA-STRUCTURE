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
    
def insertatbeg(head,val):
    newnode=Node(val,head)
    
    return newnode


if __name__ == "__main__":
    arr = [2, 5, 8, 7]

    head = create_linked_list(arr)
    
    beg_insert=insertatbeg(head,0)

    print_linked_list(beg_insert)


# class Node :
#     def __init__ (self,data,next=None):
#         self.data=data
#         self.next=next

# if __name__ == "__main__":
#     arr=input().split()
#     if not arr:
#         print("Enter any element to build an array")
#     else:
#         head=Node(arr[0])
#         temp=head
#         for i in arr[1:]:
#             temp.next=Node(i)
#             temp=temp.next
        
#         #insertion at begining
#         newnode=Node(10)
#         newnode.next=head
#         head=newnode
        
#         curr=head
#         while curr:
#             print(curr.data,"->",end=" ")
#             curr=curr.next
#         print("None")
        
        

























