class MinStack:

    def __init__(self):
        self.stack = []
        self.minn=[]

    def push(self, val: int) -> None:

        
        self.stack.append(val)

        
        
        if not self.minn or val<=self.minn[-1]:
            self.minn.append(val)
            

        


    def pop(self) -> None:
        x=self.stack.pop()

        if x==self.minn[-1]:

            self.minn.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minn[-1]