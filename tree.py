# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# time: O(V^2)
# space: O(V)

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if len(pre) == 0:
            return None
        
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        
        R = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1: R + 1], post[: R])
        root.right = self.constructFromPrePost(pre[R + 1: ], post[R: -1])
        return root
