if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    array = max(arr)
    cou = arr.count(array)
    
    for i in range(cou):
        arr.remove(array)
        
    print(max(arr))
