
def myself(name):

    age=21 
    print(f"my name is {name} and my age is {age}")
    # key and values of local veribales
    print(locals())
    # how many local veriables
    print(len(locals()))
    # find a specific local veriable if you have large number of variable
    veriable=locals()
    print(veriable['name'])
    # print(veriable['id']) key error




    

myself("shaheer")
