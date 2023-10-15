class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current_node_1=list1
        current_node_2=list2
        prev = ListNode()
        newhead = prev
        while current_node_1 != None or current_node_2 != None:
            new_node = ListNode()
            if current_node_1 == None:
                prev.next = current_node_2
                break
            if current_node_2 == None:
                prev.next = current_node_1
                break
            if current_node_1.val <= current_node_2.val:
                new_node.val=current_node_1.val
                current_node_1 = current_node_1.next
            else:
                new_node.val=current_node_2.val
                current_node_2 = current_node_2.next
            prev.next = new_node
            prev = new_node
        return newhead.next

            
