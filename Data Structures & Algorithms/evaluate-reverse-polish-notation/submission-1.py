class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #add to stack until hit operation then take previous two numbers and apply the operation
        stack = []
        ops = {
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
            "-": lambda a, b: a - b,
            "+": lambda a, b: a + b
            }
        for i in range(len(tokens)):
            if tokens[i] in ("*","/","+","-"):
                b = stack.pop()
                a = stack.pop()
                val = ops[tokens[i]](int(a),int(b))
                stack.append(val)
            else:
                stack.append(tokens[i])
        return int(stack.pop())
        