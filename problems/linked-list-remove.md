# Linked list remove node

# Problem
Given a linkedlist of integers and an integer value, delete every node of the linkedlist containing that value.

# Solution 1 - Python
```python

head = build_linked_list([1,1,4,4,5,2,1,4]);

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

head = remove_node(head, num)
```