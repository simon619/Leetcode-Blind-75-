class CLimbingStrair:

    def __init__(self):
        pass

    def climbing_with_fib(self, n):
        if n == 2 or n == 1:
            return 1
        else:
            return self.climbing_with_fib(n - 1) + self.climbing_with_fib(n - 2)


if __name__ == '__main__':
    inst = CLimbingStrair()
    n = 5
    result = inst.climbing_with_fib(n + 1)
    print(result)
