class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None

    def create(self):
        n = int(input("Enter number of nodes: "))

        if n <= 0:
            print("Please enter a valid number of nodes.")
            return

        for n in range(1, n + 1):
            val = input(f"Enter data for node {n}: ")
            self.insert(val)

    def insert(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    def show(self):
        if self.head is None:
            print("Nothing to print.")
            return

        temp = self.head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def delete(self):
        value = input("Enter value to delete: ")

        if self.head.data == value:
            self.head = self.head.next
            print("Node deleted.")
            return
        
        prev = self.head
        temp = self.head.next

        while temp is not None:
            if temp.data == value:
                prev.next = temp.next
                print("Node deleted.")
                return
            prev = temp
            temp = temp.next

        print("Node not found.")

s1= LL()

while True:
    print("\n1. Create Linked List")
    print("2. Insert Node")
    print("3. Display Linked List")
    print("4. To Delete a Node")
    print("5. Exit")

    cho = int(input("Enter your choice: "))
    if cho == 1:
        s1.create()
    elif cho == 2:
        val = input("Enter value to insert: ")
        s1.insert(val)
    elif cho == 3:
        s1.show()
    elif cho == 4:
        value=input("Enter value to remove: ")
        s1.delete
    elif cho == 5:
        print("Thank You!")










