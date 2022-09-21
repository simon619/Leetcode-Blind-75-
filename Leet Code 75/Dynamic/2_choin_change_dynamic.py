class CoinChangeDynamic:

    def __init__(self, length):
        self.max = length + 1

    def dynamic(self, coins, amount):
        dp = [self.max] * self.max
        dp[0] = 0
        for i in range(len(dp)):
            for coin in range(len(coins)):
                if i - coins[coin] >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coins[coin]])

        return dp[amount] if dp[amount] != self.max else -1


if __name__ == '__main__':
    coin_list, amount = [1, 2, 5], 11
    obj = CoinChangeDynamic(amount)
    minimum_coins = obj.dynamic(coin_list, amount)
    print(minimum_coins)
