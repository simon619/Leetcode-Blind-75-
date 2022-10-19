class Islands:

    def __init__(self):
        pass

    def numIslands(self, grid):
        visited = set()
        len_row, len_col = len(grid), len(grid[0])
        number_of_island = 0

        def dfs(r, c):
