
if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()

    if k == 0 and arr[0] > 1:
        print("1")
    elif k == 0 and arr[0] == 1:
        print("-1")
    elif k <= n - 1:
        if arr[k - 1] != arr[k]:
            print(arr[k - 1])
        else:
            print("-1")
    elif k == n:
        print(arr[k - 1])
