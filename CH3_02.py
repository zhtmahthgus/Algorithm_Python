n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
answer = 0
for i in range(1, m+1):
    if i % (k+1) == 0: answer += data[n-2]
    else: answer += data[n-1]
print(answer)