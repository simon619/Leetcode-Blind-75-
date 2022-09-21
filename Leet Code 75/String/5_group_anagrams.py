from collections import defaultdict


class GroupAna:

    def __init__(self):
        pass

    def traverse(self, words):
        dic = defaultdict(list)
        for word in words:
            word_counter = [0] * 26

            for letter in word:
                word_counter[ord(letter) % 26] += 1
            dic[tuple(word_counter)].append(word)
        return dic.values()


if __name__ == '__main__':
    obj = GroupAna()
    print(obj.traverse(["eat", "tea", "tan", "ate", "nat", "bat"]))
