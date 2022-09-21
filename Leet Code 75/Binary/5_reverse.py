class Reverse:

    def __init__(self):
        pass

    def reversing(self, or_st, rev_st, decimal, pointer):
        if pointer < 0:
            return decimal, rev_st
        else:
            rev_st += or_st[pointer]
            decimal += int(or_st[pointer]) * 2 ** pointer
            return self.reversing(or_st, rev_st, decimal, pointer - 1)


if __name__ == '__main__':
    inst = Reverse()
    st = '00000010100101000001111010011100'
    decimal, binary = inst.reversing(st, '', 0, len(st) - 1)
    print(decimal)
    print(binary)
