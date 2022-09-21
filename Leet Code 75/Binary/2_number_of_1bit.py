class NumberOf:

    def __init__(self):
        self.count = 0

    def analyze(self, bitstring, pointer):
        if pointer < 0:
            return self.count
        else:
            if bitstring[pointer] == '1':
                self.count += 1
            return self.analyze(bitstring, pointer - 1)


if __name__ == '__main__':
    inst = NumberOf()
    st = '00000000000000000000000000001011'
    result = inst.analyze(st, len(st) - 1)
    print(result)
