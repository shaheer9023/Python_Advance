def name():
    def fname():
        print("Shaheer")
    def lname():
        print("Ahmad")
    return fname, lname

f, l = name()
f(), l()