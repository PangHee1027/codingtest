from itertools import product

def solution(n, infection, edges, k) :
    graph = {1 : [], 2 : [], 3 : []}

    max_infection = 0

    for node1, node2, type in edges :
        graph[type] += [[node1, node2], [node2, node1]]

    for order in product(range(1, 4), repeat = k) :
        visited = {infection}
        for o in order :
            visited_len = len(visited)
            while True :
                for edge in graph[o] :
                    if edge[0] not in visited :
                        continue
                    if edge[1] in visited :
                        continue
                    visited.add(edge[1])
                if visited_len == len(visited) :
                    break
                visited_len =len(visited)
        max_infection = max(max_infection, len(visited))

    return max_infection