# refere striver
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Create linked list
def create_linked_list(arr):
    if not arr:
        return None

    head = Node(arr[0]) 
    current = head 

    for value in arr[1:]:
        current.next = Node(value)
        current = current.next

    return head


# Display linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


# Insertion at begining
def insertatbeg(head, val):
    newnode = Node(val, head)
    return newnode


# insertion at middle using position
def insertusingpos(head, pos, val):
    curr = head
    for i in range(1, pos - 1):
        curr = curr.next
    newnode = Node(val, curr.next)
    curr.next = newnode

    return head

#insertion at middle after a value
def insertusingvalueafter(head,pos,val):
    curr=head
    while curr.data!=pos:
        curr=curr.next
    newnode=Node(val,curr.next)
    curr.next=newnode
    return head
    
#insertion at middle Before a value
def insertusingvalueBef(head,pos,val):
    curr=head
    while curr.next.data!=pos:
        curr=curr.next
    newnode=Node(val,curr.next)
    curr.next=newnode
    return head

# insertion at end
def insertend(head, val):
    if head is None:
        return newNode
    curr = head
    while curr.next:
        curr = curr.next
    newnode = Node(val)
    curr.next = newnode
    return head


if __name__ == "__main__":
    arr = [2, 5, 8, 7]

    head = create_linked_list(arr)

    beg_insert = insertatbeg(head, 0)

    end_insert = insertend(head, 10)

    Middle_pos_insert = insertusingpos(head, 2, 88)
    
    Middle_valAfter_insert=insertusingvalueafter(head,5,99)
    
    Middle_valBef_insert=insertusingvalueBef(head,8,77)

    print("List to ll: ", end="==> ")
    print_linked_list(head)

    print("Insertion at begining: ", end="==> ")
    print_linked_list(beg_insert)

    print("Insertion at end: ", end="==> ")
    print_linked_list(end_insert)

    print("Insertion in middle using positon: ", end="==> ")
    print_linked_list(Middle_pos_insert)

    print("Instering in middle using value(After): ",end="==> ")
    print_linked_list(Middle_valAfter_insert)
    
    print("Instering in middle using value(Before): ",end="==> ")
    print_linked_list(Middle_valBef_insert)
    
    
# for all changes in same linked list
# if __name__ == "__main__":
#     arr = [2, 5, 8, 7]

#     head = create_linked_list(arr)

#     head = insertatbeg(head,0)

#     head = insertend(head,10)
#     print("List to ll: ",end="==> ")
#     print_linked_list(head)


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
