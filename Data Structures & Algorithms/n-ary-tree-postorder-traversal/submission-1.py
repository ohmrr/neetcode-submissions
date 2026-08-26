"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # result = []

        # def postorder(root):
        #     if not root:
        #         return

        #     for child in root.children:
        #         postorder(child)
        #     result.append(root.val)            

        # postorder(root)
        # return result

        result = []
        if not root:
            return result

        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if visited:
                result.append(node.val)
            else:
                stack.append((node, True))
                for child in reversed(node.children):
                    stack.append((child, False))

        return result

            

            
