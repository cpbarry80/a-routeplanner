import math


#heuristic 
def dist(origin, destination):
    return math.sqrt(( (origin[0] - destination[0])**2) + ( (origin[1] - destination[1])**2) )


def shortest_path(map, origin, destination):
    possible_branches = {origin}
    explored = set()

    start_path = {
        "node": origin,
        "current": False,
        "cost_so_far": 0,
        "cost": dist(map.intersections[origin], map.intersections[destination])}
    directions = {origin: start_path}

    while possible_branches:
        best_step = next(iter(possible_branches))
        for node in possible_branches:
            if directions[node]["cost"] < directions[best_step]["cost"]:
                best_step = node
        shortest_path = directions[best_step]

        roads = set(map.roads[shortest_path["node"]]) - explored
        possible_branches = possible_branches.union(roads)
        explored.add(shortest_path["node"])
        possible_branches.remove(shortest_path["node"])

        for node in roads:
            current = shortest_path["node"]
            estimated_cost = dist(map.intersections[node], map.intersections[destination])
            cost_so_far = shortest_path["cost_so_far"] + dist(map.intersections[node], map.intersections[shortest_path["node"]])
            total_cost = cost_so_far + estimated_cost

            if node not in directions or total_cost < directions[node]["cost"]:
                directions[node] = {
                    "node": node,
                    "current": current,
                    "cost_so_far": cost_so_far,
                    "cost": total_cost}

        if shortest_path["node"] == destination:
            steps = [destination]
            node = destination
            while directions[node]["current"]:
                steps.insert(0, directions[node]["current"])
                node = directions[node]["current"]
            return steps


