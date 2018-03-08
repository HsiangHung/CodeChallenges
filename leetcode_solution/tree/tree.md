
# Data structure: Tree 

### The tree class in Leetcode is defined as
```Python
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
```
# Pre-order
input `[10,5,15,1,6,12,20,null,2,null,8,11,13,18]`
```Python
    def preOrder(self, root):
        print root.val
        if root.left == None and root.right == None: return
        
        if root.left != None: self.preOrder(root.left)
        
        if root.right != None: self.preOrder(root.right)
```
gives
```
10
5
1
2
6
8
15
12
11
13
20
18
```

# in-order (judging binary search tree)
input `[10,5,15,1,6,12,20,null,2,null,8,11,13,18]`
```Python
    def inOrder(self, root):
        if root.left == None and root.right == None: 
            print root.val
            return
        
        if root.left != None: self.inOrder(root.left)
            
        print root.val
        
        if root.right != None: self.inOrder(root.right)
```
gives 
```
1
2
5
6
8
10
11
12
13
15
18
20
```

# Post-order 
```Python
    def postOrder(self, root):
        if root.left == None and root.right == None: 
            print root.val
            return
        
        if root.left != None: self.postOrder(root.left)
        if root.right != None: self.postOrder(root.right)

        print root.val
```
gives 
```
2
1
8
6
5
11
13
12
18
20
15
10
```
Another ways to represent preorder, inorder and postorder:
```Python
def preorder(root):
    if root != None:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root != None:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def postorder(root):
    if root != None:
        postorder(root.left)
        postorder(root.right)
        print(root.val)
```



# BFS on tree
```Python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def BreadthFirstSearch(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        h = self.getHeight(root)
        #print h
        for i in range(1, h+1):
            self.printLevel(root, i)
            
    def printLevel(self, root, level):
        if level ==0:
            return
        elif level == 1:
            print root.val
        elif level > 1:
            if root.left != None: self.printLevel(root.left, level-1)
            if root.right != None: self.printLevel(root.right, level-1)
        
    def getHeight(self, root):
        if not root.left and not root.right: return 1
        h_L = 0
        if root.left != None: h_L = self.getHeight(root.left)+1
        h_R = 0
        if root.right != None: h_R = self.getHeight(root.right)+1
        return max(h_L, h_R)
```








## Q3: Lowest Common Ancestor of a Binary Search Tree
### Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
```Python
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None: return None
        if p.val > q.val:
            return self.getNode(root, q, p)
        else:
            return self.getNode(root, p, q)
        
    def getNode(self, root, p, q):
        """
        : type root, p, q: TreeNode (q > p)
        " rtype: int
        """
        if p.val <= root.val <= q.val: return root.val
        
        if p.val <= root.val and q.val <= root.val:
            return self.getNode(root.left, p, q)
            
        if p.val >= root.val and q.val >= root.val:
            return self.getNode(root.right, p, q)
```
The following considers even not a BST, it still wors since it stores all path and it's ancestors.
```Python
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.path = {}
        self.traverse(root, str(root.val))
        a1 = self.path[p.val]
        a2 = self.path[q.val].split(',')
        for ans1 in a1.split(','):
            if ans1 in a2: return int(ans1)
            
    def traverse(self, node, path):
        self.path[node.val] = path
        if node.left == None and node.right == None: return
            
        if node.left != None:
            self.traverse(node.left, str(node.left.val)+','+path)
                
        if node.right != None:
            self.traverse(node.right, str(node.right.val)+','+path)
```
but the followings:
```Python
    def lowestCommonAncestor(self, root, p, q):
        self.path = {}
        self.wrongTraverse(root, [root.val])
        a1 = self.path[p.val]
        a2 = self.path[q.val]
        for ans1 in a1:
            if ans1 in a2: return int(ans1)
            
     def wrongTraverse(self, node, path):
        if node.left == None and node.right == None:
            self.path[node.val] = path
            return
            
        if node.left != None:
            self.path[node.val] = path
            self.wrongTraverse(node.left, path.append(node.left.val))
                
        if node.right != None:
            self.path[node.val] = path
            self.wrongTraverse(node.right, path.append(node.right.val))
```
and
```Python
    def wrongTraverse2(self, node, path):
        if node.left == None and node.right == None:
            self.path[node.val] = path
            return
            
        if node.left != None:
            self.path[node.val] = path
            path.append(node.left.val)
            self.wrongTraverse2(node.left, path)
                
        if node.right != None:
            self.path[node.val] = path
            path.append(node.right.val)
            self.wrongTraverse2(node.right, path)
```
don't work. The first one, passing ```list.append(x)``` will give ```None```, so
it won't give anything. (One can check ```print [5].append(6)``` gives ```None```).
The second one is to append ```x``` before passing ```path``` in recursion. But doing this
will append all nodes in the ```path``` list; won't generate each list for each path.





## Q8: Minimum Depth of Binary Tree
### Given a binary tree, find its minimum depth.
```Python
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        self.min = float('inf')
        self.traverse(root, 1)
        return self.min
        
    def traverse (self, root, depth):
        if root.left == None and root.right == None: 
            self.min = min(self.min, depth)
            return
    
        if root.left != None: self.traverse(root.left, depth+1)
        
        if root.right != None: self.traverse(root.right, depth+1)
```




## Q12: [Leetcode#366] Find Leaves of Binary Tree
### Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.
```Python
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None: return []
        
        self.leavesDepth = []
        while root.left != None or root.right != None:
            self.leaves = []
            self.traverse(root)
            self.leavesDepth.append(self.leaves)
            
        self.leavesDepth.append([root.val])
        return self.leavesDepth
        
    def traverse(self, root):
        if root.left == None and root.right == None: 
            self.leaves.append(root.val)
            return 'Leaves'
        
        if root.left != None:
            if self.traverse(root.left) == 'Leaves': root.left = None
            
        if root.right != None:
            if self.traverse(root.right) == 'Leaves': root.right = None
```

# Medium level

## Q2: [Leetcode#156] Binary Tree Upside Down

### Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.
```Python
class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None: return root
        self.traverse(root)
        root.left = None
        root.right = None
        return self.root
        
    def traverse(self, root):
        '''self.root is the upside down root'''
        if root.left == None: 
            self.root = root
            return
        
        if root.left != None: self.traverse(root.left)
            
        if root.right != None:
            (root.left).left = root.right
        else:
            (root.left).left = None

        (root.left).right = root
```
`self.root` is the new root after upside down (the left leaf of the bottom layer). One can define another traverse function and call the function `self.traverse2(self.root)` in the main function to check:
```Python
    def traverse2(self, root):
        print root.val
        if root.left == None and root.right == None: return
        
        if root.left != None: self.traverse2(root.left)        
        if root.right != None: self.traverse2(root.right)
```
Input `[1,2,null, 3]` returns `[3,null,2,null,1]`. Input `[1,2, 3,4,5,null,null,6,7]` returns `[6,7,4,null,null,5,2,null,null,3,1]`.



## Q4: [Leetcode#98] Validate Binary Search Tree
### Given a binary tree, determine if it is a valid binary search tree (BST).

solution 1: perform in-order traversal, and if the current root < previous, it is False
```Python
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: return True
        
        self.stack = []
        self.isValidBST = True
        self.traverse(root)
        return self.isValidBST
        
        
    def traverse(self, root):
        if root.left == None and root.right == None: 
            #print root.val
            if len(self.stack) != 0: 
                if root.val <= self.stack[len(self.stack)-1]: 
                    self.isValidBST = False
                else:
                    self.stack.pop()
                    self.stack.append(root.val)
                return
            else:
                self.stack.append(root.val)
                return
        
        if root.left != None:
            self.traverse(root.left)
            
        #print root.val
        
        if len(self.stack) != 0:
            if root.val <= self.stack[len(self.stack)-1]:
                self.isValidBST = False
                return
            else:
                self.stack.pop()
                self.stack.append(root.val)
        else:
            self.stack.append(root.val)

        if root.right != None:
            self.traverse(root.right)
```
solution 2: check if always max(left subtree) < root < min(right subtree)
```Python
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: return True
        
        if root.left == None and root.right == None: return True
        
        max_node, min_node = self.getVal(root)
        
        if max_node == 'False' and 'min_node' == False: return False
        
        if max_node!= None and min_node!=None: return min_node <= root.val <= max_node
        if max_node!='False' and min_node =='False': return root.val <= max_node
        if max_node== 'False' and min_node!='False': return min_node <= root.val
        
        return False

    
    def getVal(self, root):
        
        if root.left == None and root.right == None: return root.val, root.val
        
        max_L = None
        if root.left != None:
            max_L, min_L = self.getVal(root.left)
            if max_L == 'False' or min_L=='False': return 'False', 'False'
            
        min_R = None
        if root.right != None:
            max_R, min_R = self.getVal(root.right)
            if max_R=='False' or min_R=='False': return 'False', 'False'
    
        if max_L != None and min_R != None:
            if max_L < root.val < min_R: return max_R, min_L
        elif max_L != None and min_R == None:
            if max_L < root.val: return root.val, min_L
        elif max_L == None and min_R != None:
            if root.val < min_R: return max_R, root.val
        
        return 'False', 'False'
```