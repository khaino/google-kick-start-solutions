# Question Link
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff48/00000000003f4ed8

import operator

T = int(input())
for t in range(T):
    _qLen, wdLimit = [int(x) for x in input().split()]
    queue = []
    for idx, amt in enumerate(input().split()):
        wdCnt = int(amt) // wdLimit
        if int(amt) % wdLimit > 0:
            wdCnt += 1

        queue.append((idx + 1, wdCnt))

    queue.sort(key=operator.itemgetter(1, 0))

    output = [str(idx) for idx, _val in queue]
    print("Case #{}: {}".format(t + 1, " ".join(output)))
