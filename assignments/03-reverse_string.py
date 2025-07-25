# by using while loop
print("=============while loop===============")
name='shaheer'
print(f"original name is {name}")
reverse_name=""
count=len(name)
while count>0:
    reverse_name=reverse_name+name[count-1]
    count=count-1
print(f"reverse of name is {reverse_name}")

# by using for loop
print("=============for loop===============")
for char in name:
    reverse_name=char+reverse_name
print(f"reverse of name is {reverse_name}")

# by using slicing
print("=============Slicing===============")

print(f"reverse of name is {name[::-1]}")
