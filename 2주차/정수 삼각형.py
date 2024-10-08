# n = int(input())
# tree = []

# for _ in range(n):
#     tree.append([int(f) for f in input().split()])
#     # 각 층에 해당하는 값을 list 의 형태로 추가


# for i in range(1, n): # 이중 for 문, 0 층은 건너뜀
#     for j in range(0 , i+1): 
#         # 맨 왼쪽에 위치한 값을 경우
#         # 맨 오른쪽에 위치한 값일 경우
#         # 그 외에 위치한 경우
#         if j == 0:
#             tree[i][0] += tree[i-1][0] # 특정 위치의 값을 더함
#         elif j == i:
#             tree[i][j] += tree[i-1][j-1] # 특정 위치의 값을 더함
#         else:
#             tree[i][j] += max(tree[i-1][j-1], tree[i-1][j]) # 더했을 때 최댓값이 되는 값


# print(max(tree[n-1]))

n = int(input())
tree = []

for _ in range(n):
    tree.append(list(map(int, input().split())))

dp = [[0] * (i + 1) for i in range(n)]

dp[0][0] = tree[0][0]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + tree[i][j]
        elif j == i:
            dp[i][j] = dp[i - 1][j - 1] + tree[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + tree[i][j]

print(max(dp[n - 1]))