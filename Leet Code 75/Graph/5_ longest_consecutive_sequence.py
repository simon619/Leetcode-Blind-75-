class LCS:

    def __init__(self):
        pass

    def longestConsecutive(self, nums):
        longest = 0
        num_set = set(nums)

        for num in nums:
            if (num + 1) not in num_set:
                expand = 0
                while num - expand in num_set:
                    expand += 1
                longest = max(longest, expand)
        return longest


if __name__ == '__main__':
    obj = LCS()
    print(obj.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
