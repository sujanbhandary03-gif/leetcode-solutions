class Solution:
    def isSymmetric(self, root):
        
        def mirror(left, right):
            # Both are empty
            if not left and not right:
                return True
            
            # One is empty, other is not
            if not left or not right:
                return False
            
            # Values must be equal
            if left.val != right.val:
                return False
            
            # Check opposite sides
            return mirror(left.left, right.right) and \
                   mirror(left.right, right.left)
        
        return mirror(root.left, root.right)