class ComSum4:

    def __init__(self):
        pass

    def checking(self, list, target):
        cache_dic = {0 : 1}
        for i in range(1, target + 1):
            cache_dic[i] = 0
            for j in range(len(list)):
                cache_dic[i] += cache_dic.get(i - list[j], 0)
        return cache_dic[target]

if __name__ == '__main__':
    obj = ComSum4()
    print(obj.checking([1, 2, 3], 4))
