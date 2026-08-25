# recursiven traversal inorder-postorder-preorder---------------------------
class Node:
    def __init__(self,book):
        self.data=book
        self.left=None
        self.right=None

def create():
    book = input("Enter Book Name (or 'DONE' for no book): ")
    if book== "DONE":
        return None
    root = Node(book)
    print(f"\nEnter books in LEFT section of '{book}'")
    root.left = create()
    print(f"\nEnter books in RIGHT section of '{book}'")
    root.right = create()
    return root

def preorder(root):
    if root is not None:

        print(root.data)
        preorder(root.left)
        preorder(root.right)


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data)


root=create()
postorder(root)



