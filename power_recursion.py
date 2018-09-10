def power_recursion(a,b):
    if not type(a) == int or not type(b) == int:
        return "Please use intergers"
    if a == 0:
        return 0
    if b == 0 or a == 1:
        return 1
    if b >= 1:
        return a * power_recursion(a, b-1)
    
    b = abs(b)
    return 1 / (a * power_recursion(a, b-1))
    
print (pow(3,-4))
print (power_recursion(2,3))
print (power_recursion(3,-4))
print (power_recursion(0,3))
print (power_recursion(3,0))
print (power_recursion(1,3))
print (power_recursion('d',3))
