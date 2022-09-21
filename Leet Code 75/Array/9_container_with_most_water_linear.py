class WaterContainer:

    def __init__(self):
        pass

    def examine(self, list):
        left, right = 0, len(list) - 1
        max = 0

        while left < right:
            height = min(list[left], list[right])
            width = abs(left - right)
            area = height * width
            if area > max:
                max = area

            if list[left] < list[right]:
                left += 1
            else:
                right -= 1
        return max


if __name__ == "__main__":
    inst = WaterContainer()
    result = inst.examine([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(result)
