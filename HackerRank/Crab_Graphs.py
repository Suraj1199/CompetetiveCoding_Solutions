def crabGraphs(n, t, graph):
    cnn={x:[] for x in range(1,n+1)}
    for u,v in graph:
        cnn[u].append(v)
        cnn[v].append(u)
    nodes=set()
    for u in sorted(cnn, key=lambda s:len(cnn[s]),reverse=True):
        if u not in nodes and len(cnn[u])>=t:
            nodes.add(u)
    for u in sorted(cnn, key=lambda s:len(cnn[s]),reverse=True):
        feetofu=0
        for v in cnn[u]:
            if v not in nodes and feetofu<t:
                nodes.add(v)
                feetofu+=1
    return len(nodes)

if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n, t, m = map(int, input().rstrip().split())
        graph = []
        for _ in range(m):
            graph.append(list(map(int, input().rstrip().split())))
        result = crabGraphs(n, t, graph)
        print(result)
