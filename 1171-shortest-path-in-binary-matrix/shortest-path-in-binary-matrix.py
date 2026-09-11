class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # bfs through the thing, only adding to the queue cells that are 0
        # then we you reach the final, perform min operaiton with current min and the current value

        queue = deque([(0,0,1)])
        visited = {(0,0)}
        
        min_path_length = float('inf')

        directions = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]

        while queue:
            row, col, curr_path_length = queue.popleft()
            if grid[row][col] == 1:
                return -1
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                min_path_length = min(min_path_length, curr_path_length)

            for dx, dy in directions:
                new_row = dx + row
                new_col = dy + col
                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                    queue.append((new_row, new_col, curr_path_length + 1))
                    visited.add((new_row, new_col))
        return min_path_length if min_path_length != float('inf') else -1