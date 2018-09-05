#function to sum up items in a list
def sum_items(list_number):
    sum = 0
    for item in list_number:
        if type(item) == int:
            sum += item
        elif isinstance(item, list):
                if type(sum_items(item)) == int:
                    sum += sum_items(item)
                else:
                    return "Inside List should only have numbers"
        else:
            return "List should only have numbers"
    
    return sum 

print (sum_items([1,5,9,[3,'n']]))
print (sum_items([3,7,8,[8,9]]))