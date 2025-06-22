# shallow copy
import copy
list=[1,2,3,4,5,6]
print(list)
print(list[4])
list[4]=500
print(list)
print(id(list))


newList=copy.copy(list)
print(newList)
print(id(newList))

# ids are diff because both are in other memory location but having same values id

print(id(list[4]))
print(id(newList[4]))
# having same index values ids

#  deep copy


other_list=[1,2,3,4,5,6,]
other_new_list=copy.deepcopy(other_list)
print(other_list)
print(other_new_list)
other_list[3]=400
print(other_list)
print(other_new_list)
# now both lists and their values have different memory locations