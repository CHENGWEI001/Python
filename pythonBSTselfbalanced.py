class BSTnode:
    def __init__(self, val):
        self.val = val
        self.cnt = 1
        self.leftCnt = 0
        self.rightCnt = 0
        self.left = None
        self.right = None
        self.height = 1

class Solution:
    """
    @param A: an integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def countOfSmallerNumberII(self, A):
        ans = []
        root = None
        for n in A:
            ans.append(self.query(root, n-1))
            root = self.insert(root, n)
        return ans
    
    def getHeight(self, root):
        if not root:
            return 0
        return root.height
    
    def getBalance(self, root):
        getHeight = self.getHeight
        if not root:
            return 0
        return getHeight(root.left) - getHeight(root.right)
    
    def rightRotate(self, x):
        getHeight = self.getHeight
        y = x.left
        t2 = y.right
        x.left = t2
        y.right = x
        x.height = 1 + max(getHeight(x.left), getHeight(x.right))
        y.height = 1 + max(getHeight(y.left), getHeight(y.right))
        x.leftCnt = self.getTotalCnt(x.left)
        y.rightCnt = self.getTotalCnt(y.right)
        return y
        
    def leftRotate(self, y):
        getHeight = self.getHeight
        x = y.right
        t2 = x.left
        y.right = t2
        x.left = y
        y.height = 1 + max(getHeight(y.left), getHeight(y.right))
        x.height = 1 + max(getHeight(x.left), getHeight(x.right))
        y.rightCnt = self.getTotalCnt(y.right)
        x.leftCnt = self.getTotalCnt(x.left)
        return x
    
    def query(self, root, val):
        if not root:
            return 0
        if val == root.val:
            return root.cnt + root.leftCnt
        elif val < root.val:
            return self.query(root.left, val)
        else:
            return root.leftCnt + root.cnt + self.query(root.right, val)
    
    def getTotalCnt(self, root):
        if not root:
            return 0
        return root.cnt + root.leftCnt + root.rightCnt
    
    def insert(self, root, val):
        getHeight = self.getHeight
        if not root:
            return BSTnode(val)
        if val == root.val:
            root.cnt += 1
        elif val < root.val:
            root.left = self.insert(root.left, val)
            root.leftCnt = self.getTotalCnt(root.left)
        else:
            root.right = self.insert(root.right, val)
            root.rightCnt = self.getTotalCnt(root.right)
        
        # here need to update root's height because there might be rotation 
        # among children, left or right child height might change
        root.height = 1 + max(self.getHeight(root.left), getHeight(root.right))
        balance = self.getBalance(root)
        # left left case
        if balance > 1 and val < root.left.val:
            root = self.rightRotate(root)
        # right right case
        elif balance < -1 and val > root.right.val:
            root = self.leftRotate(root)
        # left right case
        elif balance > 1 and val > root.left.val:
            root.left = self.leftRotate(root.left)
            root = self.rightRotate(root)
        # right left case 
        elif balance < -1 and val < root.right.val:
            root.right = self.rightRotate(root.right)
            root = self.leftRotate(root)
        return root
        
