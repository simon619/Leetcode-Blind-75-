class WaterContainer:

    def __init__(self):
        pass

    def examine(self, list):
        max = 0

        for i in range(len(list) - 1):
            for j in range(i + 1, len(list)):
                width = j - i
                height = min(list[i], list[j])
                area = height * width
                if area > max:
                    max = area
        return max


if __name__ == "__main__":
    inst = WaterContainer()
    result = inst.examine([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(result)
