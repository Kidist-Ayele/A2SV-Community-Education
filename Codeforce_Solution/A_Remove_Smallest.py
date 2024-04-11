def main():
    test = int(input()) 
    for t in range(test):
        len_arr = int(input())
        arr = list(map(int, input().split()))
        arr.sort()  
        size_arr = len_arr
        i = 0
        while i <= size_arr - 2:
            if arr[i + 1] == arr[i] + 1 or arr[i+1] == arr[i]: 
                del arr[i]  
                size_arr -= 1
            else:
                i += 1
        
        if size_arr <= 1:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
