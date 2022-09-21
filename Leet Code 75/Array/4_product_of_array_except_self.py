class Product:

    def __init__(self):
        pass

    def product(self, list):
        left = [0] * len(list)
        right = [0] * len(list)
        right[len(list) - 1] = 1
        left[0] = 1

        for i in range(1, len(left)):
            left[i] = left[i - 1] * list[i - 1]

        for i in range(len(right) - 2, -1, -1):
            right[i] = right[i + 1] * list[i + 1]

        for i in range(len(list)):
            list[i] = left[i] * right[i]

        return list


if __name__ == "__main__":
    inst = Product()
    result = inst.product([1, 2, 3, 4])
    print(result)
