class ListNode:
  def __init__(self,val=0,next=None):
    self.val = val
    self.next = next
 
#make the list nodes
def list_listnode(nodes:list) -> ListNode:
  if nodes is None or len(nodes) == 0:
    return None
  new_list = ListNode(nodes[0])
  cur = new_list
  for node in nodes[1:]:
    cur.next = ListNode(node)
    cur = cur.next

  return new_list

#convert a list node back into a list
def list_listnode(head_node:ListNode) -> list:
  if head_node is None:
    return []
  list_num = []
  while head_node:
      list_num.append(head_node.val)
      head_node = head_node.next
    
  return list_num
