class ValPar:

    def __init__(self):
        pass

    def traverse(self, st):
        dic = {']': '[', '}': '{', ')': '('}
        stack = []
        for ch in st:
            if ch in dic:
                if stack and stack[len(stack) - 1] == dic[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return True if not stack else False


if __name__ == '__main__':
    obj = ValPar()
    print(obj.traverse('()[]{}'))
