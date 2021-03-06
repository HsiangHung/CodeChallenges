## [Leetcode#100] Same Tree
#
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not q and not p: return True
        if not p or not q: return False
        
        if p.val != q.val: return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        

# -----------------------------------------------------------
#  old solution, looks more tedious 
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            
            if p.val != q.val: return False
            
            if p.left and q.left and p.right and q.right:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            elif p.left and q.left and not p.right and not q.right:
                return self.isSameTree(p.left, q.left)
            elif not p.left and not q.left and p.right and q.right:
                return self.isSameTree(p.right, q.right)
            elif not p.left and not q.left and not p.right and not q.right:
                return True
            else:
                return False
            
        elif not p and not q: 
            return True
        else:
            return False
            
