class LSWRC:
    def __init__(self):
        pass

    def traverse(self, list):
        charset = set()
        left, res = 0, 0
        for right in range(len(list)):
            while list[right] in charset:
                charset.remove(list[left])
                left += 1
            charset.add(list[right])
            res = max(res, right - left + 1)
        return res


if __name__ == '__main__':
    obj = LSWRC()
    print(obj.traverse('pwwkew'))



