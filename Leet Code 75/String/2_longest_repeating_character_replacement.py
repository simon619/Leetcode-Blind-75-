class LongReapChaRe:
    def __init__(self):
        pass

    def traverse(self, lis3t, k):
        left, freq, result = 0, 0, 0
        counter = {}
        for right in range(len(list)):
            counter[list[right]] = 1 + counter.get(list[right], 0)
            freq = max(freq, counter[list[right]])

            while (right - left + 1) - freq > k:
                counter[list[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result

if __name__ == '__main__':
    obj = LongReapChaRe()
    print(obj.traverse('AABABBA', 1))

