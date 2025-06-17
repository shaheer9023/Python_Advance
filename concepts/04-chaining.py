# for one liner code  having multiple if else we use chaining

number=[-1,0,3,5,-2,0]
status=[]
for num in number:
    if num>0:
        status.append("positive")
    elif num<0:
        status.append("negetive")
    else:
        status.append("zero")
print(status)

print(["positive" if num>0 else "negetive" if num<0 else "zero" for num in number])# this line will work same as done in above lines 