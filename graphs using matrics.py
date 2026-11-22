# graphs using matrics 
class graph:
    def __init__(self):
        self.v=0
        self.e=0
        self.G=[[0 for i in range(9)] for j in range(9)] 

    def create (self):
        self.v=int(input("enter the no. of vertices: "))
        self.e=int(input("enter the no. of edges: "))


        for i in range (self.e):
            print (f"enter edge {i+1}: ")
            u= int(input("enter start vertex: "))
            v= int(input("enter end vertex: "))
            w= int(input("enter weight: "))
            self.G[u][v]=self.G[v][u]=w
            #self.G[u][v]=1 directed non weighted 

    def display(self):
        for i in range(self.v):
            for j in range(self.v):
                print (self.G[i][j], end= " ")
            print()


class stack:
    def push(self,y):
        if self.st[self.TOP]==6:
            print("stack overflow")
            return
        else:
            self.TOP +=1
            self.st[self.TOP]=y
        print("element removed" , y)
        
    def pop(self):
        if self.TOP == -1:
            print("stack underflow")
        x= self.st[self.TOP]
        self.TOP -=1
        return x

    def dfs(ob,start):
        visited=[False]*ob.v
        s=stack()
        s.push(start)
        while s.TOP != -1 :
            u=s.pop()
            if visited[u]=False:
                print(u, end= " ")
                visited [u]=True
            for v in range (ob.v-1,-1,-1):
                if (ob.G[u][v]!=0 and visited[v] == False):
                    s.push(v)

ob=graph()
ob.create()
ob.display()
