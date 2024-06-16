def total_cost_to_hire(costs, k, candidates):
    total_cost = 0
    workers = sorted(range(len(costs)), key=lambda i: costs[i])

    for i in range(k):
        total_cost += costs[workers[i]]

    return total_cost
costs = [17,12,10,2,7,2,11,20,8]
k = 3
candidates = 4

print(total_cost_to_hire(costs, k, candidates))

costs = [1,2,4,1]
k = 3
candidates = 3

print(total_cost_to_hire(costs, k, candidates))

