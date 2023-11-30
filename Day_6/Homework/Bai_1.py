
def MyMultiple(*args:int) -> int :
    '''
    this Function return a number
    '''
    if len(args) == 0:
        return 0
    
    sum=0
    for i in args:
        sum+=i
    return sum

print("MyMultiple(1, 2, 3, 4) = ",MyMultiple(1, 2, 3, 4))
print("MyMultiple(5, 5, 5) = ",MyMultiple(5, 5, 5))
print("MyMultiple(1.2, 5) = ",MyMultiple(1.2, 5))
