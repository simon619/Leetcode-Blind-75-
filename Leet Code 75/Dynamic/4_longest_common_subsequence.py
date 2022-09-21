class LCS:

    def __init__(self):
        pass

    def brute_force(self, st1, st2, index1, index2):
        if index1 == 0 or index2 == 0:
            return 0
        elif st1[index1 - 1] == st2[index2 - 1]:
            return 1 + self.brute_force(st1, st2, index1 - 1, index2 - 1)
        else:
            return max(self.brute_force(st1, st2, index1 - 1, index2), self.brute_force(st1, st2, index1, index2 - 1))


if __name__ == '__main__':
    obj = LCS()
    st1, st2 = 'abcde', 'ace'
    result = obj.brute_force(st1, st2, len(st1), len(st2))
    print(result)


