n=6
my_sum=0
for i in range(1,n):
    if(n%i==0):
        my_sum=my_sum+i
if (my_sum==n):
    print("the number is perfect number")
else:
    print("the number is not a perfect number")
    
