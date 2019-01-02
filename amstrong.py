n=int(input("Enter the amstrong number:::::::"))
s=0
num=n
while(n>0):
    r=n%10
    s=s+(r**3)
    n=n/10
if(s==num):
    print(n,"is amstrong number")
else:
    print(n,"is not amstrong")
