if __name__ == '__main__':
    N = int(input())
    list1 = []
    for i in range(N):
        inp = input().split()
        for i in range(1,len(inp)):
            inp[i] =  int(inp[i])
            
        if inp[0]== "append":
            list1.append(inp[1])
        if inp[0] == "insert":
            list1.insert(inp[1],inp[2])
        elif inp[0] == "remove":
            list1.remove(inp[1])        
        elif inp[0] == "pop":
            list1.pop()
        elif inp[0] == "sort":
            list1.sort()
        elif inp[0] == "reverse":
            list1.reverse()
        elif inp[0] == "print":
            print(list1)
            
