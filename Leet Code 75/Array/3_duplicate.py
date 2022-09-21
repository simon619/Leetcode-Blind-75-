class Duplicate:

    def __init__(self):
        pass

    def duplicate_finder(self, list):

        def insearch(list, pointer, dic):
            if pointer == len(list):
                return False

            elif list[pointer] in dic:
                return True

            else:
                dic[list[pointer]] = pointer
                pointer += 1
                return insearch(list, pointer, dic)

        dic = {}
        return insearch(list, 0, dic)


if __name__ == "__main__":
    inst = Duplicate()
    result = inst.duplicate_finder([1, 2, 3, 4])
    print(result)
