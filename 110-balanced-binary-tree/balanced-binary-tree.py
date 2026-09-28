class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        if not root:
            return True

        left_height = self.height(root.left)
        right_height = self.height(root.right)

        if abs(left_height - right_height) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root):
        if not root:
            return 0

        return 1 + max(
            self.height(root.left),
            self.height(root.right)
        )