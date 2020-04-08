def listSum(l, s=0):
    if len(l)==0:
        return s
    s+=l[0]
    return listSum(l[1:], s)

print(listSum([])) # 0
print(listSum([42])) # 42
print(listSum([3,1,5,2])) # 11
