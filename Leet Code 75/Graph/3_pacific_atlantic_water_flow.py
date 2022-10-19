class PacificAtlantic:
    def __init__(self):
        pass

    def operation(self, list):
        len_row, len_col = len(list), len(list[0])
        pacific, atlantic = set(), set()

        def dfs(row, col, visited, prev_node):
            if row < 0 or col < 0 or row >= len_row or col >= len_col or ((row, col) in visited) or list[row][
                col] < prev_node:
                return
            else:
                visited.add((row, col))
                dfs(row + 1, col, visited, list[row][col])
                dfs(row - 1, col, visited, list[row][col])
                dfs(row, col + 1, visited, list[row][col])
                dfs(row, col - 1, visited, list[row][col])

        for c in range(len_col):
            dfs(0, c, pacific, list[0][c])
            dfs(len_row - 1, c, atlantic, list[len_row - 1][c])

        for r in range(len_row):
            dfs(r, 0, pacific, list[r][0])
            dfs(r, len_col - 1, atlantic, list[r][len_col - 1])
        print(pacific)
        print(atlantic)
        result = [(row, col) for row in range(len_row) for col in range(len_col) if
                  (row, col) in pacific and (row, col) in atlantic]
        return result


if __name__ == '__main__':
    obj = PacificAtlantic()
    print(obj.operation([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
