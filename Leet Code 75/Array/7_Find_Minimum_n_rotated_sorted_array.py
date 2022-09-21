class Find:

    def __init__(self):
        pass

    def find(self, list, left, right):

        while left < right:
            mid = (right + left) // 2

            if mid == right:
                right -= 1
            elif list[mid] > list[right]:
                left = mid + 1
            else:
                right = mid

        return list[right], right

    def rotate_array(self, list):
        value, index = self.find(list, 0, len(list) - 1)
        list1 = list[:index]
        list2 = list[index:]
        list = list2 + list1
        return list, index


if __name__ == "__main__":
    inst = Find()
    result, index = inst.rotate_array([4,5,6,7,0,1,2])
    print(result)
    print(f'If it was rotated: {index} times')
