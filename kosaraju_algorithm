# previous solution
def kosaraju(adj, rev_adj):
    def dfs(node, graph, visited, stack):
        visited[node] = True
        for neigh in graph[node]:
            if not visited[neigh]:
                dfs(neigh, graph, visited, stack)
        stack.append(node)

    def reverse_dfs(node, graph, visited, component):
        visited[node] = True
        component.append(node)
        for neigh in graph[node]:
            if not visited[neigh]:
                reverse_dfs(neigh, graph, visited, component)

    n = len(adj)
    visited = [False] * n
    stack = []
    
    for i in range(n):
        if not visited[i]:
            dfs(i, adj, visited, stack)
    
    visited = [False] * n
    scc = []
    while stack:
        node = stack.pop()
        if not visited[node]:
            component = []
            reverse_dfs(node, rev_adj, visited, component)
            scc.append(component)
    
    return scc
