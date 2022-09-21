class LIS:

    def __init__(self):
        pass

    def counting(self, list):
        tail_list = [0] * len(list)
        length = 0
        for num in range(len(list)):
            left, right = 0, length
            while left != right:
                mid = (left + right) // 2
                if tail_list[mid] < list[num]:
                    left = mid + 1
                else:
                    right = mid
            tail_list[left] = list[num]
            length = max(left + 1, length)
        return length


if __name__ == '__main__':
    obj = LIS()
    list = [2, 8, 9, 5, 6, 7, 1]
    print(obj.counting(list))

