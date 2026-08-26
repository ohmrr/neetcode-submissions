# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # LEFT -> RIGHT -> ROOT
        # result = []

        # def postorder(root):
        #     if not root:
        #         return 

        #     postorder(root.left)
        #     postorder(root.right)
        #     result.append(root.val)

        # postorder(root)
        # return result

        result, stack = [], []
        curr = root

        while curr or stack:
            if curr:
                result.append(curr.val)
                stack.append(curr.left)
                curr = curr.right
            else:
                curr = stack.pop()

        return result[::-1]