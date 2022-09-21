class LongestPalindromicSubstring:

    def __init__(self):
        pass

    def for_odd(self, list):
        result = ''
        result_length = 0
        for i in range(len(list)):
            left, right = i, i
            while left >= 0 and right < len(list) and list[left] == list[right]:
                if (right - left + 1) > result_length:
                    result = list[left: right + 1]
                    result_length = right - left + 1
                left -= 1
                right += 1
        return result

    def for_even(self, list):
        result = ''
        result_length = 0
        for i in range(len(list)):
            left, right = i, i + 1
            while left >= 0 and right < len(list) and list[left] == list[right]:
                if (right - left + 1) > result_length:
                    result = list[left: right + 1]
                    result_length = right - left + 1
                left -= 1
                right += 1
        return result


if __name__ == '__main__':
    obj = LongestPalindromicSubstring()
    list = 'cbbd'
    print(obj.for_odd(list)) if len(list) % 2 == 1 else print(obj.for_even(list))
