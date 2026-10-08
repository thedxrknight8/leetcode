# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        # for a particular root, we maintain a max and a min parameter
        # essentially, for that root, float('-inf') and float('inf') initially
        # for the left dfs, then max should be root. if right dfs, then min should be root. 
        # so for every dfs, we keep checking. if we get to a null value, we have fully dfs'd, and we can return true
        # otherwise, we must return false (have an or operation with left and right result as return case)


        def dfs(root, mi, ma):
            if not root:
                return True

            left = right = False
            if mi < root.val < ma:
                left = dfs(root.left, mi, root.val)
                right = dfs(root.right, root.val, ma)
            
            return left and right
        return dfs(root, float('-inf'), float('inf'))
            