def lowest_product(string):
    nums=len(string)

    if nums < 4:
        return "Number is too small"
        
    if '0' in string:
        return 0
    
    numbers = list(map(lambda x:int(x),string))
    
    v0,v1,v2,v3 = numbers[0:4]
    least=(v0*v1*v2*v3)
    for i in range(4,nums):
        n=numbers[i]
        v0,v1,v2,v3=v1,v2,v3,n
        value=(v0*v1*v2*v3)
        if value < least:
            least=value
    return least
