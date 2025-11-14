#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 12:51:19 2025

@author: LiamBiam
"""

###############################################
############### Trees and Tries ###############
###############################################

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

##############################################
###### Binary Trees Iterative Traversal ######
##############################################

# Pre-Order Traversal

root = None

def preorderTraversal_Iterative(root):
    
    '''
    
    Pre Order Traversal is basically go left until you can't then after reaching the 
    end of a branch then go right if possible and continue going left until you can't 
    and backtrack when you can't go left or right anymore... idk its simple but hard to explain
    
    stack ensures you follow the most recent root node added if its not None (end of branch)
    so when we add the left node if it exists we will visit it next, and again, and again,
    until you go as far as you can go in the left branch then you go right and then backtrack
    to previous nodes and then go right and repeat the left priority process
    
    summary: top --> bottom left --> right
    
    '''
    
    if not root:        # for when theres no tree to begin with lol
        return []
    
    stack = [root]      # for DFS process
    ans = []            # root.val values
    while stack:
        root = stack.pop()
        ans.append(root.val)
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
            
    return ans
        
# In-Order Traversal

root = None

def inorderTraversal_Iterative(root):
    
    '''

    this is a level more difficult than Pre-Order Traversal
    because it appends values in the order of what is left most 
    then what the root above is, before going right next

    stack gets built up while moving thru nodes to the bottom left
    re-visits parent node when child node is None or is called from the stack
    proceeds to go right, then resumes going left building up stack

    summary: bottom left --> root --> right
             append values from left to right via  DFS algorithm

    '''

    stack = []
    ans = []

    while stack or root:        # why {or root}? compared to Pre-Order Traversal
        while root:             # because root node existing is a pre-requisite fir stack build-up
            stack.append(root)  # stack gets built up by appending not None child roots
            root = root.left    # loop ends when a child node turns out to be None or Null
        root = stack.pop()      # root node (or parent node) is popped from the stack 
        ans.append(root.val)    # value is appended from order of left to right in tree strucuture
        root = root.right       # finally node focused on next becomes the next right node
    return ans

# Post-Order Traversal 

root = None

def levelorderTraversal_Iterative(root):
    
    '''
    
    use queue DS for BFS to access one level at a time
    when there are no more levels queue will be empty and while loop will stop
    ans will be returned listing from left to right every val for nodes on each level
    
    
    summary: bottom left --> right --> root
    
    
    '''
    
    ans = []
    if not root:
        return ans
    
    level = 0
    queue = [root]
    
    while queue:
        ans.append([])
        for i in range(len(queue)):
            root = queue.pop(0)
            ans[level].append(root.val)
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
    
        level += 1
        
    return ans

##############################################
###### Binary Trees Recursive Traversal ######
##############################################

# Pre-Order Traversal

root = None

def preorderTraversal_Recursive(root):
    
    
    '''
    
    summary: root --> bottom left --> right
    
    '''
    
    ans = []
    if not root:
        return ans

    def helper(root):
        if root: 
            ans.append(root.val)
            helper(root.left)
            helper(root.right)
    
    helper(root)
    return ans
        
# In-Order Traversal

root = None

def inorderTraversal_Recursive(root):
    
    '''

    summary: bottom left --> root --> right

    '''
    
    ans = []
    if not root:
        return ans

    def helper(root):
        if root: 
            helper(root.left)
            ans.append(root.val)
            helper(root.right)
    
    helper(root)
    return ans

# Post-Order Traversal 

root = None

def postorderTraversal_Recursive(root):
    
    '''
    
    summary: bottom left --> right --> root
    
    
    '''
    
    ans = []
    if not root:
        return ans

    def helper(root):
        if root: 
            helper(root.left)
            helper(root.right)
            ans.append(root.val)
    
    helper(root)
    return ans

# Post-Order Traversal (Hack Method)

root = None

def postorderTraversal_Recursive_Hack(root):
    
    '''
    
    hack relies on copying the pre-order traversal 
    and reversing the tranversal anser
    
    summary: bottom left --> right --> root
    
    
    '''
    
    ans = []
    if not root:
        return ans

    def helper(root):
        if root: 
            ans.append(root.val)
            helper(root.right)
            helper(root.left)
    
    helper(root)
    return ans[::-1]

# Level-Order Traversal (BFS)

root = None

def levelorderTraversal_Recursive(root):
    
    '''
    
    summary: bottom left --> right --> root
    
    
    '''
    
    ans = []
    if not root:
        return ans
    
    def helper(root, level):
        
        if len(ans) == level:            # append new empty list if needed
            ans.append([])
            
        ans[level].append(root.val)      # add this levels root.val to level list
        
        if root.left:                       # go left until you reach a None node
            helper(root.left, level + 1)
        if root.right:
            helper(root.right, level + 1)   # go right until you reach a None node
        
    helper(root, 0)
    return ans

##########################################
###### Various Binary Tree Problems ######
##########################################

# Maximum Depth of Binary Tree (Just Reuse Level Order Traversal, return len(ans))

root = None

def maxDepth_BFS(root):
    
    '''
    
    Just Return the Length of the Array of Arrays to Determine Depth
    BFS Traversal (or just level order traversal)
    
    '''
    
    ans = []
    if not root:
        return 0
    
    def helper(root, level):
        
        if len(ans) == level:            # append new empty list if needed
            ans.append([])
            
        ans[level].append(root.val)      # add this levels root.val to level list
        
        if root.left:                       # go left until you reach a None node
            helper(root.left, level + 1)
        if root.right:
            helper(root.right, level + 1)   # go right until you reach a None node
        
    helper(root, 0)
    return len(ans)

# Maximum Depth of Binary Tree (The Simpler Way, Lower Space Complexity)

root = None

def maxDepth_DFS(self, root):

    '''
    
    DFS Traversal while recording maximum depth along the way on each side
    Similar to Dynamic Programming, Explore All (Both) Options, return the max
    
    '''

    if not root:
        return 0
    l_depth = self.maxDepth_DFS(root.left)
    r_depth = self.maxDepth_DFS(root.right)
    return max(l_depth, r_depth) + 1

# Symmetric Tree

root = None

def isSymmetric(self, root):
        
    return self.isMirror(root, root)

def isMirror(self, left, right):
    
    '''
    
    if statements catch null nodes (no node.val), 
    True if both null, False is only one is null (cond 0)
    
    value comparison must show equal values (cond 1)
    
    recursively call outer and inner subtree nodes and compare them
    using the if statements for edge cases (one or more nodes don't exist, cond 2)
    
    (cond 2 cont.) values must be equal for each subtree all the way until the bottom
    
    like Dynamic Programming, if one False occurs everything is False
    if all cases turn out to be True then the binary tree is symetrical
    
    '''
    
    if not left and not right:  # both next nodes aren't there
        return True
    if not left or not right:   # one next node is there, but one is, not symmetric
        return False
    
    return (left.val == right.val      # if both exist (False and False Cond), compare vals
           and self.isMirror(left.right, right.left)    # next subtree, inner directions
           and self.isMirror(left.left, right.right))   # next subtree, outer directions

# Path Sum

root = None

def hasPathSum(self, root, targetSum):
    
    
    '''
    
    similar to symetric tree, also a case of dynamic programming 
    explore all possible options and if one is True, the or condition
    will trigger all other or logic to return True (A or B or C or D, etc)
    
    we are suppose to check if a root to leaf sum matches targetSum
    so we need an if statement that checks for a leaf condition,
    which is True when the left and right branches are null 
    
    naturally the recursive logic will explore below the leaf statements,
    simply return False and this won't effect the overall algorithm
    
    '''
    
    if not root:                                        # return False if Node doesn't exist
        return False
    
    targetSum -= root.val                               # subtract from targetSum
    
    if not root.left and not root.right:                # leaf condition
        return targetSum == 0
    
    return (self.hasPathSum(root.left, targetSum)       # check bool state of each branch
            or self.hasPathSum(root.right, targetSum))
    

# Count Univalue Subtrees

def countUnivalSubtrees(self, root):
    
    '''

    all leaf nodes are subtrees, so we need a base case that
    checks for this condition, and additionally

    l_true and r_true must consistently be true for a subtree 
    to be univalued, this means the subtree node is null or the 
    same value or the subtree is not univalued

    if either l_true or r_true is False then self.count isn't 
    incimented and we return False, if the parent node value 
    doesn't match the nodes left or right values (child nodes)
    even in the l_true and r_true values are True, we return False

    '''

    self.count = 0

    def dfs(root):

        if not root:     # check for all leaf nodes, all univalue subtrees
            return True

        l_true = dfs(root.left)
        r_true = dfs(root.right)

        if l_true and r_true:   # False if theres a diff in parent and (left or right) vals
            if root.left and root.val != root.left.val:
                return False
            if root.right and root.val != root.right.val:
                return False

            self.count += 1

            return True

        return False 

    dfs(root)
    return self.count

# Construct Binary Tree from Inorder and Postorder Traversal (re-used at top of code)

postorder = [9,15,7,20,3]
inorder = [9,3,15,20,7]

def buildTree(postorder, inorder):
    
    '''
    
    Constructing TreeNode DS' from inorder and (pre-order or post-order) requires using
    knowledge from each traversal algorithm to deduce where the root is. In-Order has the
    root somewhere in the middle, and post order has the root at the end of the traversal list.
    
    We use information from the Post-Order algorithm to split the lists in two,
    when the l_inorder index defining the left side of the in-order exceeds the right,
    we know we have previously reached a leaf node, so its child node is defined as None.
    
    Difference between this and pre-order is that we pop() or (pop(n-1)) of pop(0)
    and that we start with building the right subtrees before we build the left subtrees
    
    '''
    
    def helper(l_inorder, r_inorder):

        if l_inorder > r_inorder:       # cannot construct subtrees with empty sublists
            return None

        value = postorder.pop(0)         # pop from post-order to get root
        root = TreeNode(value)          # create node for root
        index = index_hash[value]       # divide list based on index location

        # lists should be sublists 
        root.right = helper(index + 1, r_inorder)     # connect root to right node
        root.left = helper(l_inorder, index - 1)    # connect root to left node 
        return root                                 # return TreeNode

    index_hash = {value:index for index, value in enumerate(inorder)}
    return helper(0, len(inorder) - 1)

root_post = buildTree(postorder, inorder)

# Construct Binary Tree from Preorder and Inorder Traversal (re-used at top of code)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

def buildTree(preorder, inorder):
    
    '''
    
    Constructing TreeNode DS' from inorder and (pre-order or post-order) requires using
    knowledge from each traversal algorithm to deduce where the root is. In-Order has the
    root somewhere in the middle, and post order has the root at the end of the traversal list.
    
    We use information from the Pre-Order algorithm to split the lists in two,
    when the l_inorder index defining the left side of the in-order exceeds the right,
    we know we have previously reached a leaf node, so its child node is defined as None.
    
    Difference between this and post-order is that we pop(0) instead of (pop(n-1)) or pop()
    and that we start with building the left subtrees before we build the right subtrees
    
    '''
    
    def helper(l_inorder, r_inorder):

        if l_inorder > r_inorder:       # cannot construct subtrees with empty sublists
            return None

        value = preorder.pop(0)         # pop from pre-order to get root
        root = TreeNode(value)          # create node for root
        index = index_hash[value]       # divide list based on index location

        # lists should be sublists 
        root.left = helper(l_inorder, index - 1)     # connect root to right node
        root.right = helper(index + 1, r_inorder)    # connect root to left node 
        return root                                 # return TreeNode

    index_hash = {value:index for index, value in enumerate(inorder)}
    return helper(0, len(inorder) - 1)

root_pre = buildTree(preorder, inorder)

####################################
######## Binary Search Tree ########
####################################

# Validate Binary Search Tree (Iterative)

def isValidBST(root):
    
    '''
    
    all we need to do is do inorder tranversal and return False if the next 
    value we traverse is not equal to or greater than the previous value
    
    inorder traversal for BSTs will return the values in ascending order
    
    I basically took the inorder traversal iterative algorithm and added 
    a check for if the next value is greater than or equal to the previous value.
    
    I also struggled with the concept of -2**31 < root.val < 2**31, that root.val
    could be negative. I could've used -math.inf but I knew 10**10 > 2**31 so....
    
    '''
    
    if not root.left and not root.right:
        return True
    
    stack = []
    value = -10**10
    
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if root.val <= value:
            return False
        value = root.val
        root = root.right
        
    return True

# Inorder Successor in BST 

def inorderSuccessor(root, p):
    
    '''
    
    In this situation, we flag when we've found p, when root.val == p.val,
    where I initialized next_node = False but make it True when this condition is met.
    
    The next node visited in inorder traversal will be the successor,
    so I just put a next_node == True check 
    which returns the root after its popped from the stack.
    
    '''
    
    if not root.left and not root.right:
        return None
    
    stack = []
    next_node = False
    
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if next_node:
            return root
        if root.val == p.val:
            next_node = True
        root = root.right
        
    return None

# Binary Search Tree Iterator (Recursive Inorder Traversal to Build List)

class BSTIterator:

    def __init__(self, root):
        self.traversal = []
        self.index = -1
        self.inorder(root)
        
    def inorder(self, root):
        if not root:
            return None
        self.inorder(root.left)
        self.traversal.append(root.val)
        self.inorder(root.right)

    def next(self) -> int:
        self.index += 1
        return self.traversal[self.index]

    def hasNext(self) -> bool:
        return self.index < len(self.traversal) - 1

# Search in a Binary Search Tree (Iterative)

def searchBST(root, val):
    
    stack = []
    
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if root.val == val:
            return root
        root = root.right

    return None

# Search in a Binary Search Tree (Recursive)

def searchBST(root, val):
    
    if not root or root.val == val:
        return root
    
    if val < root.val:
        return searchBST(root.left, val)
    
    return searchBST(root.right, val)

# Insert into a Binary Search Tree (Iterative)

def insertIntoBST(root, val):
    
    '''
    
    temporarily assign node to root, so we can alter root through node
    and later return root once we find a place for val using node to explore
    
    1) go left or right through node based on whether val is lt or gt node.val
    --> left subtree vals must be lt or equal to node.val
    --> right subtree vals must be gt or equal to node.val
    2) we must insert at a leaf node, or one with node.left or node.right that is None
    based on whether we should be inserting left or right (conditions meantioned in 1)
    3) once we meet criteria for inserting left or right, we assign
    node.left or node.right to a new node; TreeNode(val), and return root
    
    if there is nowhere to insert val we return TreeNode(val)
    
    '''
    
    node = root
    
    while node:

        if val <= node.val:
            if not node.left:
                node.left = TreeNode(val)
                return root
            else:
                node = node.left

        if val > node.val:
            if not node.right:
                node.right = TreeNode(val)
                return root
            else:
                node = node.right

    return TreeNode(val)

# Insert into a Binary Search Tree (Recursive)

def insertIntoBST(self, root, val):
    
    if not root:
        return TreeNode(val)
    
    if val <= root.val:
        root.left = self.insertIntoBST(root.left, val)
        
    if val > root.val:
        root.right = self.insertIntoBST(root.right, val)
        
    return root

# Delete Node in a BST

def successor(self, root):
    root = root.right
    while root.left:
        root = root.left
    return root.val

def predecessor(self, root):
    root = root.left
    while root.right:
        root = root.right
    return root.val

def deleteNode(self, root, key):

    '''

    this algorithm takes advantage of the simple approach to restructuring a 
    binary search tree when we delete a node from the tree. the hard part 
    is maintaining the properties of a BST, but the trouble is mainly fixed
    by only proceeding downward using another property of a BST, the inorder
    traversal occurs in ascending order; [1,2,7,11,12,13,25,33,34,36,40]
    
    the only time we implement changes is when root.val == key, otherwise
    we go left or right down the tree to find the key according to BST properties
    
    1) if 13 is a leaf node, we just re-assign its value to None, then recursively
    do each call back up the root, where we're essentially just returning the root to 
    itself for every recursive call until we return the new tree without node having node.val (13)
    
    2) if there is a root.right at the key, regardless of if there's a left, we can reconstruct
    the tree by finding the successor, which is the next highest value in traversal order.
    to find that we go bottom left, then root, then right to traverse a BST. the next highest 
    value is right of the root, then bottom left (until you reach a root.left == None). 
    
    Note... we recursively reconstruct the tree by setting the key root.val to the successor val
    then find where the original successor val root is and delete it, replacing it with its successor, 
    until we eventually get to a case where the value we are deleting is a leaf node, and finally 
    go up thru the recursive stack returning root as root until we reach the 1st call and return root
    
    3) finally, the last case where there isn't a right child node, and its not a leaf,
    we just do the same thing but backwards, meaning finding the predecessor, reassigning 
    the current node.val to the successor val, then recursively calling again and again
    until we reach the leaf case where we just delete by assigning its value to None
    
    '''    

    if not root:
        return None

    if key > root.val:
        root.right = self.deleteNode(root.right, key)

    if key < root.val:
        root.left = self.deleteNode(root.left, key)

    if key == root.val:
        if not (root.left or root.right):
            root = None
        elif root.right:
            root.val = self.successor(root)
            root.right = self.deleteNode(root.right, root.val)
        else:
            root.val = self.predecessor(root)
            root.left = self.deleteNode(root.left, root.val)

    return root

# Kth Largest Element in a Stream (11/12 cases passed, fails due to imbalanced BST)

class TreeNode:
    def __init__(self, val, count, left=None, right=None):
        self.val = val
        self.count = count
        self.left = left
        self.right = right

class KthLargest:

    def __init__(self, k, nums):
        self.root = None
        self.k = k
        for num in nums:
            self.root = self.insert(self.root, num)

    def add(self, val: int) -> int:
        self.root = self.insert(self.root, val)
        return self.searchKth(self.root, self.k)
    
    def insert(self, root, val):
        if not root:
            return TreeNode(val, 1)
        if val > root.val:
            root.right = self.insert(root.right, val)
        else:
            root.left = self.insert(root.left, val)
        root.count += 1
        return root

    def searchKth(self, root, k):
        m = root.right.count if root.right else 0
        if k == m + 1:
            return root.val
        elif k <= m:
            return self.searchKth(root.right, k)
        else:
            return self.searchKth(root.left, k - m - 1)

# Lowest Common Ancestor of a Binary Search Tree

def lowestCommonAncestor(self, root, p, q):
    
    ''' 
    
    basically if the nodes value is between p and q (or q and p) then by definition 
    of a BST it is the lowest common anscestor. otherwise, we either go left or right 
    recursively based on whether p and q's values are to the left or right of the BST
    
    '''
    
    if p.val > root.val and q.val > root.val:
        return self.lowestCommonAncestor(root.right, p, q)
    elif p.val < root.val and q.val < root.val:
        return self.lowestCommonAncestor(root.left, p, q)
    else:
        return root
    
# Contains Duplicate III



###############################################################
######## Tries Basic Operations and Practical Problems ########
###############################################################

# Next Problem







# Next Problem







# Next Problem







# Next Problem







# Next Problem







# Next Problem







