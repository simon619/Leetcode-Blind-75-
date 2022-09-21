class HouseRob:

    def __init__(self):
        pass

    def robbing(self, houses):
        next, prev = 0, 0

        for house in houses:
            temp = max(next + house, prev)
            next = prev
            prev = temp

        return prev


if __name__ == '__main__':
    obj = HouseRob()
    print(obj.robbing([1, 2, 3, 1]))
