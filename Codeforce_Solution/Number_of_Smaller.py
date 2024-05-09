n, m = map(int, input().split())

arr1 = []
arr2 = []
result = []

arr1 = [int(i) for i in input().split()]
arr2 = [int(i) for i in input().split()]

left = right = 0
while left < n and right < m :
    if arr1[left] >= arr2[right]:
        result.append(left)
        right += 1
    else:
        left += 1

diff = m - len(result)
result.extend([left]*diff)

print(*result)

