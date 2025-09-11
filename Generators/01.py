# creating geberator function

# def gen():
#     yield "Shaheer Ahmad"
#     yield "i am 22 years old"

# g=gen()
# print(g)
# print(type(g))
# # print(next(g))
# # print(next(g))

# for element in g:
#     print(element)



def countDown(number):
    print("count Down begins here : ")
    while number>0:
        yield number
        number=number-1

c=countDown(10)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))