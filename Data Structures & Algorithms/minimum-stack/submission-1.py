class MinStack:

    def __init__(self):
        MinStack.stack = []
        MinStack.stack2 = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        #print("pushed " +str(val) +" onto stack" + str(self.stack))
        if len(self.stack2) == 0:
            self.stack2.append(val)
        else:
            self.stack2.append(min(val,self.stack2[-1]))
        

    def pop(self) -> None:
        #print("popped " +str(self.stack[-1]) +" off stack"+ str(self.stack))
        self.stack = self.stack[0:-1]
        self.stack2 = self.stack2[0:-1]
        #print("new stack is " + str(self.stack))

    def top(self) -> int:
        #print("top = " + str(self.stack[-1]) +" of"+ str(self.stack))
        return self.stack[-1]
        
        

    def getMin(self) -> int:
        #print("min = " +str(self.minimum)+" of"+ str(self.stack))
        return self.stack2[-1]
        
