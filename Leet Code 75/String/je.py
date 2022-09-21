from collections import defaultdict

if __name__ == '__main__':
    info_dic = defaultdict(list)
    lowest_grade, second_lowest_grade = 99999, 99999
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score < lowest_grade:
            temp = lowest_grade
            second_lowest_grade = temp
            lowest_grade = score
        if lowest_grade < score < second_lowest_grade:
            second_lowest_grade = score
        info_dic[score].append(name)

    sorted = info_dic[second_lowest_grade]
    sorted.sort()

    for i in sorted:
        print(i)
