import heapq


def min_cost(elements):
    cost = 0
    heapq.heapify(elements)

    while len(elements) > 1:
        print('Current ropes (sorted):', elements)
        first_shortest = heapq.heappop(elements)
        second_shortest = heapq.heappop(elements)
        cost_connected = first_shortest + second_shortest
        print(f'Connection: "{first_shortest}" to "{second_shortest}". Cost: {cost_connected}.\n')
        
        cost += cost_connected
        heapq.heappush(elements, cost_connected)
    
    return cost


ropes = [7, 1, 3, 5, 2]

print(f'Minimum cost of ropes connection: {min_cost(ropes)}.')
