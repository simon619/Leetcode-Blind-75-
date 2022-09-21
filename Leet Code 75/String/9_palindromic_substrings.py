class PalindromicSubstrings:

    def __init__(self):
        pass

    def traverse(self, list, left, right):
        res = 0
        while left >= 0 and right < len(list) and list[left] == list[right]:
            res += 1
            left -= 1
            right += 1
        return res

    def checking(self, list):
        result = 0
        for i in range(len(list)):
            result += self.traverse(list, i, i)
            result += self.traverse(list, i, i + 1)
        return result


if __name__ == '__main__':
    obj = PalindromicSubstrings()
    print(obj.checking('aaab'))
