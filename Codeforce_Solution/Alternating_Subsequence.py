test = int(input())

for _ in range(test):
    n = int(input())
    arr = [int(i) for i in input().split()]
    result = 0
    left = 0
    while left < n:
        current = arr[left]
        right = left + 1
        while right < n and current * arr[right] > 0:
            current = max(current, arr[right])
            right += 1
        result += current
        left = right
    print(result)
