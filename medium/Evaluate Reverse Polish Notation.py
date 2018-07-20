class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        top = 0
        for token in tokens:
            if token.strip("-").isdigit():
                stack.append(token)
                top += 1
            else:
                num2 = int(stack.pop(-1))
                num1 = int(stack.pop(-1))
                top -= 2
                equation = str(round(num1))+token+str(round(num2))
                result = int(eval(equation))
                stack.append(result)
                top += 1
        if top == 1:
            return int(stack[0])
        else:
            print "error:", stack
    def evalRPN2(self, tokens):
        import operator
        op = {
            "+": lambda y,x:x+y,
            "-": lambda y,x:x-y,
            "*": lambda y,x:x*y,
            "/": lambda y,x:int(operator.truediv(x,y))
              }
        stack = []
        for token in tokens:
            if token not in op:
                stack.append(token)
            else:
                res = op[token](int(stack.pop(-1)), int(stack.pop(-1)))
                stack.append(res)
        return int(stack[-1])


if __name__ == '__main__':
    s = Solution()
    print s.evalRPN2(["2","1","+","3","*"])