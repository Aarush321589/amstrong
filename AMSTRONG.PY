#take the input from the user
num=int(input("enter a number"))
sum=0
temp=num
while temp>0:
    digit=temp% 10
    sum+=digit**3
    temp//=10
#display the result
if num==sum:
    print(num,"is an armstrong number"  )
else:
    print(num,"is not a amstrong number")