class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
  
        for x in range(len(tokens)):
            if tokens[x] == "+":
                second = stack.pop()
                first = stack.pop()
                stack.append(first + second)
            elif tokens[x] == "-":
                second = stack.pop()
                first = stack.pop()
                stack.append(first - second)
            elif tokens[x] == "*":
                second = stack.pop()
                first = stack.pop()
                stack.append(first * second)
            elif tokens[x] == "/":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first / second))
                print(second, first, " division equals ",(first // second) )
            else:
                stack.append(int(tokens[x]))
        return stack[0]


        
