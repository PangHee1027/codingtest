import sys

sys.setrecursionlimit(10000000)

def solution(grid):
    state_dict = {"S" : {"up" : "up", "down" : "down", "left" : "left", "right" : "right"},
                  "L" : {"up" : "left", "down" : "right", "left" : "down", "right" : "up"},
                  "R" : {"up" : "right", "down" : "left", "left" : "up", "right" : "down"}             
                }
    
    n = len(grid)
    m = len(grid[0])

    state_count = {}
    visited = set()
    answer = []

    def dfs(state, count) :
        count += 1
        if state_count.get(state, 0) :
            return count - state_count.get(state)
        state_count[state] = count
        visited.add(state)
        cell, d = state
        i, j = cell
        direction = state_dict[grid[i][j]][d]

        match direction :
            case 'up' :
                i -= 1
                if i < 0 :
                    i = n - 1
            case 'down' :
                i += 1
                if i >= n :
                    i = 0
            case 'left' :
                j -= 1
                if j < 0 :
                    j = m - 1
            case 'right' :
                j += 1
                if j >= m :
                    j = 0

        cell = (i, j)
        state = (cell, direction)
                                                         
        return dfs(state, count)

    for i in range(n) :
        for j in range(m) :
            for direction in ("up", "down", "left", "right") :
                state = ((i, j), direction)
                if state in visited :
                    continue
                cycle = dfs(state, 0)
                answer.append(cycle)
    
    return sorted(answer)