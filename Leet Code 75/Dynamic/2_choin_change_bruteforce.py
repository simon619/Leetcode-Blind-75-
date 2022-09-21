class CoinChangeBF:
    def __init__(self):
        self.max = 9999
        pass

    def brute_force(self, coins, amount):
        minimum = self.max
        if amount < 0:
            return -1
        elif amount == 0:
            return 0
        else:
            for i in range(len(coins)):
                total = 1 + self.brute_force(coins, amount - coins[i])
                if total == 0:
                    continue
                minimum = min(minimum, total)
        return minimum if minimum != self.max else -1


if __name__ == '__main__':
    obj = CoinChangeBF()
    coin_list, amount = [2], 3
    minimum_coins = obj.brute_force(coin_list, amount)
    print(minimum_coins)


