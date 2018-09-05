def power_recursion(a,b):
    if type(a) == int and type(b) == int:
        if b == 0:
            return 1
        elif b >= 1:
            return a * power_recursion(a,b-1)
        else:
            return "The number to be powered shouldnot be negative"
    else:
        return "Please use intergers"

print (power_recursion(2,3))
print (power_recursion('d',3))
