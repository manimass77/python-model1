num=int(input('enter the number:'))
sum=0
temp=num
while temp>0:
    number=temp%10
    sum+=number
    temp=temp//10
print("sum of numbers:", sum)
