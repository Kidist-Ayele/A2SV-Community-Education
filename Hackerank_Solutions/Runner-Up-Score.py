if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sorted_list = sorted(arr)
    size = len(sorted_list)
    for right in range(size-1, -1, -1):
        if sorted_list[right] == sorted_list[right-1]:
            right = right-1
        else:
            break
        
    print(sorted_list[right-1])