class WordBreak:

    def __init__(self):
        pass

    def check(self, st, word_dic):
        dp = [False] * (len(st) + 1)
        dp[0] = True

        for i in range(1, len(st) + 1):
            for j in range(0, i):
                if st[j: i] in word_dic and dp[j]:
                    dp[i] = True
                    break

        return dp[len(dp) - 1]


if __name__ == '__main__':
    obj = WordBreak()
    print(obj.check("catsandog", ["cats", "dog", "sand", "and", "cat"]))
