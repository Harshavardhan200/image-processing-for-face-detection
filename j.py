from itertools import combinations
def min_sum_queries (N, A, Q, queries):
    # Write your code here
    temp = []
    data = []
    sub = []
    for k in range(Q):

        temp = A[queries[k][0]-1:queries[k][1]]
        temp.sort()
        sum = 0
        for i in combinations(temp, queries[k][2]):
            sum = 0
            for j in range(len(i)):
                sum += i[j]
            data.append(sum)
        for i in combinations(temp, queries[k][3]):
            sum = 0
            for j in range(len(i)):
                sum += i[j]
            data.append(sum)
        sub.append(min(data))
    return sub

T = 1
for _ in range(T):
    N = 5
    A = [0,-9,2,-9,3]
    Q = 8
    queries = [[2,4,1,3],[2,5,1,4],[2,4,1,1],[2,4,1,3],[1,5,1,3],[2,4,1,2],[2,5,1,4],[1,4,1,2]]
    out_ = min_sum_queries(N, A, Q, queries)
    print(' '.join(map(str, out_)))
