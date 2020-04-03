T = int(input())
for t in range(T):
    n = int(input())
    taken_boy = []
    taken_girl = []
    for z in range(n):
        taken_boy.append(0)
        taken_girl.append(0)
    for k in range(n):
        grooms = list(map(int, input().split()))
        del grooms[0]
        for s in range(len(grooms)):
            if taken_boy[grooms[s]] == 0:
                taken_boy[grooms[s]] = 1
                taken_girl[k] = 1
    for i in range(len(taken_girl)):
        if taken_girl[i] == 0:
            for a in range(len(taken_boy)):
                if taken_boy[a] == 0:
                    print('IMPROVE')
                    print(taken_girl[i], taken_boy[k])
    if min(taken_boy) == 1:
        print('OPTIMAL')
