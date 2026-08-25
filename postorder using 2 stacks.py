
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def create():
    n=int(input("Enter data to create node :"))
    if n==0:
        return None
    root=Node(n) #object creation
    print(f"Enter left of {n}")
    root.left=create()
    print(f"Enter right of {n}")
    root.right=create()
    return root

def postorder(root):
    if root is None:
        return

    s1 = []
    s2 = []

    s1.append(root)

    while s1:
        node = s1.pop()
        s2.append(node)

        if node.left is not None:
            s1.append(node.left)
            print("data moved to s1")

        if node.right is not None:
            s1.append(node.right)
            print("data moved to s1")

    while s2:
        node = s2.pop()
        print(node.data, end=" ")
        print("s2 is empty")

root=create()
postorder(root)