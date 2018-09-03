#function to sum up items in a list
def sum_items(a):
    sum = 0
    sum_inside_list = 0
    for x in a:
        if type(x) == int:
            sum +=x
        
        elif isinstance(x, list):
            for i in x:
                if type(i) == int:
                    sum_inside_list += i
                else:
                    return "Inside List should only have numbers"
        else:
            return "List should only have numbers"
    
    return sum + sum_inside_list

print (sum_items([1,5,9,[3,'n']]))
print (sum_items([3,7,8,[8,9]]))