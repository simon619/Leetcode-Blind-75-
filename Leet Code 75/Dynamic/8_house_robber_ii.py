class HouseRob2:

    def __init__(self):
        pass

    def robbing(self, list):
        return max(list[0], self.check(list[1:]), self.check(list[:-1]))

    def check(self, houses):
        next, prev = 0, 0

        for house in houses:
            temp = max(next + house, prev)
            next = prev
            prev = temp

        return prev


if __name__ == '__main__':
    obj = HouseRob2()
    print(obj.robbing([2, 3, 2]))
