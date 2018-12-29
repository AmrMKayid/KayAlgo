import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        import queue
        q = queue.Queue()
        if root != None:
            q.put(root)
            while not q.empty():
                tree = q.get()
                print(tree.data, end=' ')
                if tree.left != None:
                    q.put(tree.left)
                if tree.right != None:
                    q.put(tree.right)


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
