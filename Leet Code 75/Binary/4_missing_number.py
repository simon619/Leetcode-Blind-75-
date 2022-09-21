class MissingNumber:

    def __init__(self):
        pass

    def find_the_number(self, list):
        temp = [False] * (len(list) + 1)
        for i in range(len(list)):
            temp[list[i]] = True

        for i in range(len(temp)):
            if not temp[i]:
                return i


if __name__ == '__main__':
    inst = MissingNumber()
    result = inst.find_the_number([9, 6, 4, 2, 3, 5, 7, 0, 1])
    print(result)
