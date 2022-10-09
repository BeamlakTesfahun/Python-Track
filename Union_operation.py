e = int(input())
e1 = set(map(int,input().split()))
f = int(input())
f1 = set(map(int,input().split()))
u = e1.union(f1)
counter = 0
for i in u:
    counter += 1
print(counter)
