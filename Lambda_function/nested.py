# # lambda num1:return lambda num2:return num1*num2
# function=lambda num1:lambda num2: num1*num2
# print(function(5)(6))

# another example
# square=lambda num1:num1**2
# f1=lambda function:lambda num2:function(num2)+num2
# print(f1(square)(5))

cube=lambda number:number**3
func1=lambda cube:lambda num:cube(num)+num
func2=func1(cube) # return lambda num:cube(num)+num = func2
print(func2(5)) #return cube(num)+num

