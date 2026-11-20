class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack=[]
        

        for i in tokens:
            if i in '+-*/':
                a=stack.pop()
                b=stack.pop()

                if i=='+':
                    stack.append(a+b)

                if i=='-':
                    stack.append(b-a)

                if i=='*':
                    stack.append(a*b)

                if i=='/':
                    stack.append(int(b/a))

            else:
                stack.append(int(i))

        return stack[-1]

        