def maths(num1,num2):
    sub=num1-num2
    add=num1+num2
    return sub,add
print((maths(20,30)))
sub,add=(maths(20,30)) # its like sub=20-30 , add=20+30
print(f"sub is : {sub}")
print(f"add is : {add}")