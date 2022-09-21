class Counting:

    def __init__(self):
        self.list = []
        self.count = 0

    def int_to_bin(self, number, st):
        if number == 0:
            return st
        else:
            st += str(number % 2)
            number = number // 2
            return self.int_to_bin(number, st)

    def one_counter(self, bitstring, pointer):
        if pointer < 0:
            return self.count
        else:
            if bitstring[pointer] == '1':
                self.count += 1
            return self.one_counter(bitstring, pointer - 1)

    def list_operation(self, n):
        self.list = [0] * n
        for i in range(n):
            temp = str(self.int_to_bin(i, ''))
            self.count = 0
            self.list[i] = self.one_counter(temp, len(temp) - 1)


if __name__ == '__main__':
    inst = Counting()
    inst.list_operation(5 + 1)
    print(inst.list)
