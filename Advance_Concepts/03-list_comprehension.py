# example
number=[1,2,3,4,5,6,7,8,9]
# print("\n".join(str(num*num) for num in number))


# names=["shaheer","ahmad","anas","bilal"]
# print("\n".join(f"{position} : {values}" for position,values in enumerate(names,start=1)))

print([num*num for num in number])

# print square if number is even
print([num*num for num in number if num%2==0])

#  square of number divisible by 2 and 3

print([num*num for num in number if num%2==0 if num%3==0])

# agar even h to square otherwise cube
print("\n".join(str(num**2) if num%2==0 else str(num**3) for num in number))


name="shaheer" 
# for pos,value in enumerate(name,start=1):
#     print(f"{pos} : {value}")

print("\n".join(f"{pos} : {value}" for pos,value in enumerate(name,start=1)))