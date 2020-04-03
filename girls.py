T = int(input())
for t in range(T):
    n = int(input())
    dict_marriage = {}
    brides = []
    gr = []
    for z in range(1, n + 1):
        brides.append(z)
        gr.append(z)
    for k in range(1, n + 1):
        grooms = list(map(int, input().split()))
        del grooms[0]
        for s in range(len(grooms)):
            if grooms[s] not in dict_marriage:
                dict_marriage[grooms[s]] = k
                # print(grooms[s], k)
                for v in range(len(brides)):
                    if brides[v] == k:
                        # print(brides[v])
                        del brides[v]
                        break
                for w in range(len(gr)):
                    if gr[w] == grooms[s]:
                        # print(brides[v])
                        del gr[w]
                        break
                break
    if not brides:
        print('OPTIMAL')
    else:
        print('IMPROVE')
        print(brides[0], gr[0])

    # print(dict_marriage)