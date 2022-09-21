class JumpGame:

    def __init__(self):
        pass

    def jump(self, list):
        goal_state = len(list) - 1

        for i in range(len(list) - 1, -1, -1):
            if list[i] + i >= goal_state:
                goal_state = i
        return True if goal_state == 0 else False


if __name__ == '__main__':
    obj = JumpGame()
    print(obj.jump([2, 3, 1, 1, 4]))
