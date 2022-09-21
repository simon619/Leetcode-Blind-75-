class ValAna:

    def __init__(self):
        pass

    def traverse(self, l1, l2, counter):
        if counter == len(l1):
            return True
        else:
            res = True
            if l1[counter] not in l2:
                res = False
            return res and self.traverse(l1, l2, counter + 1)

    def checking(self, list1, list2):
        if len(list1) != len(list2):
            return False
        else:
            return self.traverse(list1, list2, 0)


if __name__ == '__main__':
    obj = ValAna()
    print(obj.checking('rat', 'car'))
