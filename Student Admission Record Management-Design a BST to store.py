class Node:
    def __init__(self, admission_no):
        self.admission_no = admission_no
        self.left = None
        self.right = None


# Insert student admission number
def insert(root, admission_no):
    if root is None:
        return Node(admission_no)

    if admission_no < root.admission_no:
        root.left = insert(root.left, admission_no)
    elif admission_no > root.admission_no:
        root.right = insert(root.right, admission_no)

    return root


# Search for a student
def search(root, admission_no):
    if root is None:
        return False

    if root.admission_no == admission_no:
        return True

    if admission_no < root.admission_no:
        return search(root.left, admission_no)
    else:
        return search(root.right, admission_no)


# Inorder Traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.admission_no, end=" ")
        inorder(root.right)


# Main Program
root = None

user_input = input("Enter Student Admission Numbers separated by space: ")
students = user_input.split()

for student in students:
    root = insert(root, int(student))


# Display BST in sorted order
print("\nStudent Admission Records (Inorder): ", end="")
inorder(root)


# Search Student
key = int(input("\n\nEnter Admission Number to search: "))

if search(root, key):
    print("Student Admission Number", key, "is found.")
else:
    print("Student Admission Number", key, "is not found.")