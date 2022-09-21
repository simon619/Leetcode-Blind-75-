class DecodeWays:

    def __init__(self):
        pass

    def decode(self, list):
        dic = {}
        dic[len(list)] = 1
        for i in range(len(list) - 1, -1, -1):
            if list[i] == '0':
                dic[i] = 0
            else:
                dic[i] = dic[i + 1]
            if i + 1 < len(list) and (list[i] == '1' or (list[i] == '2' and list[i + 1] in '0123456')):
                dic[i] += dic[i + 2]
        return dic[0]


if __name__ == '__main__':
    obj = DecodeWays()
    print(obj.decode('121'))
