
class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

# returns head of linked list with elements added
def build_linked_list(arr):
  if len(arr) == 0:
    return None
  head = Node(arr[0])
  walker = head
  for i in range(1, len(arr)):
    walker.next = Node(arr[i])
    walker = walker.next
  return head

# pretty print linked list
def print_linked_list(head):
  while head:
    print head.val,
    print "->",
    head = head.next
  print "null"