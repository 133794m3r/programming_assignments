def solution(number):
    sum=0
    for i in range(3,number):
        if i >= 15 and i % 15 == 0:
            print(i)
            sum+=i
        elif i >= 5 and i % 5 == 0:
            print(i)
            sum+=i
        elif i % 3 == 0:
            print(i)
            sum+=i
    
    return sum
