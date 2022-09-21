class Profit:

    def __init__(self):
        pass

    def max_profit(self, list):
        maxprofit = 0

        for i in range(len(list) - 1):
            for j in range(i + 1, len(list)):
                if list[j] - list[i] > maxprofit:
                    maxprofit = list[j] - list[i]

        return maxprofit


if __name__ == "__main__":
    inst = Profit()
    result = inst.max_profit([7, 6, 4, 3, 1])
    print(result)
