#----------------------------------------------STACK-------------------------------------------------------------

class stack:
    def __init__(self):
        self.stack=[]

    def push (self, item):
        self.stack.append(item)
        print(f"{item}pushed to stack")

    def safe_pop(self):
        if len(self.stack) ==0:
            print("stack is empty")
            return None
        else:
            return self.stack.pop()
        
    def display(self):
        print("stack:", self.stack)

s= stack()
s.push(10)
s.push(20)
s.push(30)

s.display()

print("popped:", s.safe_pop())
print("popped:", s.safe_pop())
print("popped:", s.safe_pop())

print("popped:" , s.safe_pop())


print("")

#---------------------------------------------------------QUEUE--------------------------------------------------------------


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} enqueued to queue")

    def safe_dequeue(self):
        if len(self.queue) == 0:
            print("queue is empty")
            return None
        else:
            return self.queue.pop(0)   
        
    def display(self):
        print("queue:", self.queue)


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

print("dequeued:", q.safe_dequeue())
print("dequeued:", q.safe_dequeue())
print("dequeued:", q.safe_dequeue())

print("dequeued:", q.safe_dequeue())