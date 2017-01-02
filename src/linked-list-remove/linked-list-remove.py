
from linkedlist import build_linked_list, print_linked_list

head0 = build_linked_list([]);
head1 = build_linked_list([1])
head2 = build_linked_list([1,1,4,4,5,2,1,4]);
head3 = build_linked_list([4,5,2,1,1,4]);
head4 = build_linked_list([1,1,1]);
head5 = build_linked_list([1,4,1,1,2,1,1,1]);
num = 1

def remove_node(head, num):
  # empty
  if not head:
    return head
  # single node
  if head.next == None:
    if head.val == num:
      return None
    else:
      return head
  # remove matching nodes from the start
  while head and head.val == num:
    head = head.next
  # remove matching nodes to the end
  walker = head
  while walker:
    if walker.next and walker.next.val == num:
      walker.next = walker.next.next
    else:
      walker = walker.next
  return head

# before remove 
print_linked_list(head0)
print_linked_list(head1)
print_linked_list(head2)
print_linked_list(head3)
print_linked_list(head4)
print_linked_list(head5)

print "-----------------"

head0 = remove_node(head0, num)
head1 = remove_node(head1, num)
head2 = remove_node(head2, num)
head3 = remove_node(head3, num)
head4 = remove_node(head4, num)
head5 = remove_node(head5, num)

# after remove
print_linked_list(head0)
print_linked_list(head1)
print_linked_list(head2)
print_linked_list(head3)
print_linked_list(head4)
print_linked_list(head5)