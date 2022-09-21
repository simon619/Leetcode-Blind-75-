class MinimumWindowSubstring:

    def __init__(self):
        self.inf = 99999

    def winsliding(self, list1, list2):
        slide_window, counter = {}, {}
        for i in range(len(list2)):
            counter[list2[i]] = 1 + counter.get(list2[i], 0)

        need, have = len(counter), 0
        result, result_length = [-1, -1], self.inf
        left = 0
        for right in range(len(list1)):
            slide_window[list1[right]] = 1 + slide_window.get(list1[right], 0)

            if list1[right] in list2 and slide_window[list1[right]] == counter[list1[right]]:
                have += 1

            while have == need:
                if (right - left + 1) < result_length:
                    result_length = right - left + 1
                    result = [left, right]

                slide_window[list1[left]] -= 1
                if list1[left] in list2 and slide_window[list1[left]] < counter[list1[left]]:
                    have -= 1
                left += 1
        left, right = result[0], result[1]
        return list1[left: right + 1] if result_length <= self.inf else ""

if __name__ == '__main__':
    obj = MinimumWindowSubstring()
    print(obj.winsliding('ADOBECODEBANC', 'ABC'))
