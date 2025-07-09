n=list(map(int,input().split()))
x=n[::-1]
y=0
for i in n:
    y+=i
z=y//len(n)
print(x,y,z)
