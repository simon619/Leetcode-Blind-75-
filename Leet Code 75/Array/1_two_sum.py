class Solution(object):

    def __init__(self):
        pass

    # Optimised
    def two_sum_dic(self, nums, target):

        dic = {}
        exists = False
        for i in range(len(nums)):
            if target - nums[i] in dic:
                exists = True
                return [dic[target - nums[i]], i]
            else:
                dic[nums[i]] = i

        if not exists:
            return "Sorry Not Found"

    # Brute Force
    def two_sum_brute_force(self, nums, target):
        exists = False

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] is target:
                    exists = True
                    return [[i][j]]

        if not exists:
            return "Sorry Not Found"


if __name__ == "__main__":
    ins1 = Solution()
    result = ins1.two_sum_dic([3, 2, 7], 6)
    print(result)

    ins2 = Solution()
    result = ins2.two_sum_dic([7, 2, 4, 5, 6], 8)
    print(result)
