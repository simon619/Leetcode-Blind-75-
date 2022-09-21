class SumOfInt:

    def __init__(self):
        pass

    def summing(self, number, count):
        if count == 0:
            return number
        else:
            number += 1
            return self.summing(number, count - 1)


if __name__ == "__main__":
    inst = SumOfInt()
    result = inst.summing(5, 3)
    print(result)

