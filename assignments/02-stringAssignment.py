# write program to count number of vovels in string
string="my name is shaheer ahmad"
vovels=["a","e","i","o","u"]
count=0
for char in string:
    if char in vovels:
        count+=1
print(f"total vovels are : {count}")