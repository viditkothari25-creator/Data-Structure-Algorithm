class Node:
    def __init__(self, account_no):
        self.account_no = account_no
        self.left = None
        self.right = None


def insert(root, account_no):
    if not root:
        return Node(account_no)

    if account_no < root.account_no:
        root.left = insert(root.left, account_no)
    elif account_no > root.account_no:
        root.right = insert(root.right, account_no)

    return root


# 1. Recursive Inorder Traversal
def recursive_inorder(root, result):
    if root:
        recursive_inorder(root.left, result)
        result.append(root.account_no)
        recursive_inorder(root.right, result)

    return result


# 2. Non-Recursive (Iterative) Inorder Traversal using Stack
def non_recursive_inorder(root):
    result = []
    stack = []
    current = root

    while current or stack:

        # Reach the leftmost node
        while current:
            stack.append(current)
            current = current.left

        # Pop and record the node
        current = stack.pop()
        result.append(current.account_no)

        # Move to the right subtree
        current = current.right

    return result


# Create BST
root = None

user_input = input("Enter Bank Account Numbers separated by space: ")
accounts = user_input.split()

for acc in accounts:
    root = insert(root, int(acc))


# Perform Traversals
rec_result = recursive_inorder(root, [])
non_rec_result = non_recursive_inorder(root)


# Display Results
print("\nRecursive Inorder Output:     ", rec_result)
print("Non-Recursive Inorder Output:", non_rec_result)


# Verification
if rec_result == non_rec_result:
    print("\n[VERIFICATION SUCCESSFUL] Both traversal methods produce identical results!")
else:
    print("\n[VERIFICATION FAILED] Results do not match.")