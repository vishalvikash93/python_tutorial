#syntax
# map(function,iterable)


# function - is a function which is applying on each items
# iterable- list,tuple,set,


lst=[9,4,2,5]

def method1(lst):
    temp=[]
    for i in lst:
        temp.append(i**2)
    return temp
# print(method1(lst))

def square(x):
    return x**2
# res=list(map(square,lst))
# print(res)

res1=list(map(lambda j:j**2,lst))
print(f'res1:{res1}')
# syntax
# lambda param: implementation


# map_res=list(map(lambda k : k**2 , lst))
# print(map_res)

# # syntax
add_number=lambda param1,param2 : param1+param2
# print(add_number(45,5))




add= lambda num1,num2 : num1+num2
res=add(2,3)
# print(res)


def add_number(param1,param2):
    res=param1+param2
    return res
add_number(2,3)
# lambda
# map
# filter
# reduce
# generators
# decorator
