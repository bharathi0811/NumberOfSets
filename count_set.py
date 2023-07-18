def check_bit(n,i):
    if n&(1<<i)!=0:
        return True
    else:
        return False

count=0
n= int(input())
for i in range(64):
    if check_bit(n,i):
        count+=1
print(count)