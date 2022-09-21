class TreeSum:

    def __init__(self):
        pass

    def tree_sum(self, list):
        list.sort()
        right = len(list) - 1
        result = []

        for i in range(len(list) - 2):
            left = i + 1
            while left < right:
                sum = list[i] + list[left] + list[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                if sum == 0:
                    temp = [list[i], list[left], list[right]]
                    if temp not in result:
                        result.append(temp)
                    left += 1
        return result


if __name__ == "__main__":
    inst = TreeSum()
    result = inst.tree_sum([-1, 0, 1, 2, -1, -4])
    print(result)

