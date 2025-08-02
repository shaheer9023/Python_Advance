# veriable length positional arguments
def addition(*num):
    print(num) # this will give us tuples
    return sum(num)
print(addition(10,20,30))
print(addition(10,20))
print(addition(10,20,40))



# veriable length positional arguments
def addition(**num):
    print(num) # this will give us dictionary
    return sum(num.values())
print(addition(num1=10,num2=20,num3=30))
print(addition(num1=10,num2=20))
print(addition(num1=10,num2=20,num3=40))
import math as m
def product(*num,**nums):
    return m.prod(num)*m.prod(nums.values())

print(product(10,20,30,n1=40,n2=50,n3=60))

