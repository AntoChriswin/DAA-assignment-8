def dfs(node, parent, net_income):
    max_net_income = net_income

    for adjacent_node in tree[node]:
        if adjacent_node != parent:
            if amount[adjacent_node] < 0:
                net_income -= abs(amount[adjacent_node])
            else:
                net_income += amount[adjacent_node] // 2

            max_net_income = max(max_net_income, dfs(adjacent_node, node, net_income))

            if amount[adjacent_node] < 0:
                net_income += abs(amount[adjacent_node])
            else:
                net_income -= amount[adjacent_node] // 2

    return max_net_income


# Example usage
edges = [[0, 1], [1, 2], [1, 3], [3, 4]]
bob = 3
amount = [-2, 4, 2, -4, 6]

n = len(amount)
tree = [[] for _ in range(n)]

for edge in edges:
    u, v = edge
    tree[u].append(v)
    tree[v].append(u)

max_net_income = dfs(0, -1, 0)
print(max_net_income)
