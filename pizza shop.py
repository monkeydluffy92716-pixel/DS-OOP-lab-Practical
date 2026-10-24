import heapq

# Graph: location -> [(neighbor, travel_time)]
graph = {
    'P': [('A', 4), ('B', 2)],
    'A': [('P', 4), ('C', 5), ('B', 1)],
    'B': [('P', 2), ('A', 1), ('D', 7)],
    'C': [('A', 5), ('D', 3), ('E', 6)],
    'D': [('B', 7), ('C', 3), ('E', 2)],
    'E': [('C', 6), ('D', 2)]
}

def dijkstra(start):
    distance = {node: float('inf') for node in graph}
    distance[start] = 0

    pq = [(0, start)]

    while pq:
        time, current = heapq.heappop(pq)

        if time > distance[current]:
            continue

        for neighbor, travel_time in graph[current]:
            new_time = time + travel_time

            if new_time < distance[neighbor]:
                distance[neighbor] = new_time
                heapq.heappush(pq, (new_time, neighbor))

    return distance

# Find minimum delivery times from the pizza shop
result = dijkstra('P')

print("Minimum delivery times:")
for location, time in result.items():
    print(location, ":", time, "minutes")