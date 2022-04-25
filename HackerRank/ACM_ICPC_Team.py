def acmTeam(topic):
    d = []
    resdic = {}
    m = 0
    for t in topic:
        temp = set()
        for i in range(len(t)):
            if t[i]=='1':
                temp.add(i)
        d.append(temp.copy())
    # print(d)
    for i in range(len(d)-1):
        for j in range(i+1,len(d)):
            l = len(d[i].union(d[j]))
            m = max(m,l)
            resdic[l]=resdic.get(l,0)+1
    return [m,resdic[m]]

if __name__ == '__main__':
    n, m = map(int, input().rstrip().split())
    topic = []
    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)
    result = acmTeam(topic)
    print('\n'.join(map(str, result)))
