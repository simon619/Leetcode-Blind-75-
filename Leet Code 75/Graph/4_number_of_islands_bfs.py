class Islands:

    def __init__(self):
        pass

    def numIslands(self, grid):
        visited = set()
        len_row, len_col = len(grid), len(grid[0])
        number_of_island = 0

        def bfs(r, c):
            queue = [(r, c)]
            visited.add((r, c))
            while queue:
                row, col = queue.pop(0)
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for i, j in directions:
                    rick, morty = row + i, col + j
                    if 0 <= rick < len_row and 0 <= morty < len_col and (rick, morty) not in visited and grid[rick][
                        morty] == '1':
                        queue.append((rick, morty))
                        visited.add((rick, morty))

        for ro in range(len_row):
            for co in range(len_col):
                if (ro, co) not in visited and grid[ro][co] == '1':
                    bfs(ro, co)
                    number_of_island += 1
        return number_of_island


if __name__ == '__main__':
    obj = Islands()
    print(obj.numIslands([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))
