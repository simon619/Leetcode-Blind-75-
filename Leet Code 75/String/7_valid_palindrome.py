class Palindrome:

    def __init__(self):
        pass

    def checking(self, list, left, right):
        if left == right:
            return True
        else:
            return list[left] == list[right] and self.checking(list, left + 1, right - 1)


if __name__ == '__main__':
    st = ' '
    new_st = ''
    for i in st:
        if i.isalnum():
            new_st += i.lower()
    obj = Palindrome()
    if len(new_st) == 0:
        print(True)
    else:
        print(obj.checking(new_st, 0, len(new_st) - 1))

