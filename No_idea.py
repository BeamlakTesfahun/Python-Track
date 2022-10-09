n,m= map(int,input().split())
arr = list(map(int,input().split()))
a = set(map(int,input().split()))
b= set(map(int,input().split()))
numa = 0
numb = 0
for i in arr:
    if i in a:
        numa += 1
    elif i in b:
        numb -= 1
print(int(numa + numb))

