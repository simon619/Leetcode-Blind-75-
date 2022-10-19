class CourseSchedule:

    def __init__(self):
        pass

    def can_finish(self, numCourse, preq_detail):
        dic = {i: [] for i in range(numCourse)}
        for course, preq in preq_detail:
            dic[course].append(preq)

        visited_node = set()
        def dfs(course):
            if course in visited_node:
                return False
            if not dic[course]:
                return True

            visited_node.add(course)
            for preq in dic[course]:
                if not dfs(preq):
                    return False
            dic[course] = []
            visited_node.remove(course)
            return True
        for course in range(numCourse):
            if not dfs(course):
                return False
        return True


if __name__ == '__main__':
    obj = CourseSchedule()
    # list = [[0, 1], [0, 2], [1, 4], [1, 3], [3, 4]]
    list = [[0, 1], [1, 3], [1, 2], [2, 3], [3, 0]]
    print(obj.can_finish(len(list), list))



