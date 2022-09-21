class MaxSubArrPro:

    def __init__(self):
        pass

    def crosscalculation(self, low, mid, high, list):
        left_product = -99999
        product = 1
        for i in range(mid, low - 1, -1):
            product *= list[i]
            if product > left_product:
                left_product = product
                max_left = i

        right_product = -99999
        product = 1
        for j in range(mid + 1, high + 1):
            product *= list[j]
            if product > right_product:
                right_product = product
                max_right = j

        return max_left, max_right, left_product * right_product

    def divideandconquer(self, low, high, list):
        if low == high:
            return low, high, list[low]
        else:
            mid = (low + high) // 2
            left_low, left_high, left_product = self.divideandconquer(low, mid, list)
            right_low, right_high, right_product = self.divideandconquer(mid + 1, high, list)
            cross_low, cross_high, cross_product = self.crosscalculation(low, mid, high, list)
            if left_product > right_product and left_product > cross_product:
                return left_low, left_high, left_product
            elif right_product > left_product and right_product > cross_product:
                return right_low, right_high, right_product
            else:
                return cross_low, cross_high, cross_product


if __name__ == '__main__':
    obj = MaxSubArrPro()
    list = [2, 3, -2, 4]
    low, high, sum = obj.divideandconquer(0, len(list) - 1, list)
    print(sum)
