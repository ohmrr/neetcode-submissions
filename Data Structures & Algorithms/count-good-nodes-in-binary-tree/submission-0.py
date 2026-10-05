# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        num_good = 0
        queue = deque([(root, root.val)]) # (node, max_value)

        while queue:
            node, max_seen = queue.popleft()

            if node.val >= max_seen:
                num_good += 1
                max_seen = node.val

            if node.left:
                queue.append((node.left, max_seen))
            
            if node.right:
                queue.append((node.right, max_seen))

        return num_good