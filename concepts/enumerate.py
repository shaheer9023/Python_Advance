name=["shaheer","ahmad","shoaib","usman","soban"]
print(enumerate(name))
print(list(enumerate(name,start=1)))# make list of name with counter
print(dict(list(enumerate(name,start=1))))# make dict of name with counter

for position,element in enumerate(name,start=1):
    print(f"{position} : {element}")

