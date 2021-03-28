class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_linked_list(root: ListNode) -> ListNode:
    """function to reverse linked list in-place.
    @param root (ListNode): root node of the given linked list
    @return cur_node (ListNode): tail node of the given linked list
    """
    if root is None:
        return
    
    prev_node = None
    cur_node = root
    next_node = root.next
    
    while cur_node and next_node:
        cur_node.next = prev_node
        prev_node = cur_node
        cur_node = next_node
        next_node = next_node.next
    
    cur_node.next = prev_node
    return cur_node
