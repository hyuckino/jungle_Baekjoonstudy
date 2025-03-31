import sys
sys.setrecursionlimit(100000)
class Node:
    def __init__(self,key,left=None,right=None):
        self.key=key
        self.left=left
        self.right=right
        
root = None  

def add_key(node,key):
    if node is None:
        return Node(key)
    
    if key < node.key:
        node.left = add_key(node.left, key)
    elif key > node.key:
        node.right = add_key(node.right, key)
        
    return node

def add(key):
    global root
    root = add_key(root, key)
    
nums=[]
while True:                            
    try:
        nums.append(int(sys.stdin.readline()))
    except:
        break
for i in nums:
    add(i)
    
def postorder(root):
    if root.left!=None:
        postorder(root.left)
    if root.right!=None:
        postorder(root.right)
    print(root.key)
    
postorder(root)