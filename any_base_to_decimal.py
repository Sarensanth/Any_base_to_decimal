def any_base_to_decimal(number,base):

    decimal=0
    i=0
    while number>0:
        last=number%10
        n=last*base**i
        decimal+=n
        number=number//10
        i+=1
    return decimal

number=int(input())
base=int(input())
print(any_base_to_decimal(number,base))
