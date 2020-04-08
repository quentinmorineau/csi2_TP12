def pow(x,n):
    if n==0:
        return 1
    if n==1:
        return x
    return x*pow(x,n-1)


print(pow(42, 0)) # 1
print(pow(1, 10)) # 1
print(pow(2, 5)) # 32
print(pow(7, 2)) # 49
