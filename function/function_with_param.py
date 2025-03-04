from operator import length_hint


def add(*args):
    print(f'args type:{type(args)}')
    return list(args)


res = add(1,6,3,5,7,'s',[2,4,2])
print(res)

def test(a,b,*args,**kwargs):
    x=10
    print(x)
    print(kwargs)
print(x)
# test(2,5,2,5,7,24,53.29,90,fname="suman",lname="kumari")


# Calling the function
# sum_result = add(5, 3)
# print(sum_result)  # Output: 8
# print(type(sum_result))


# 1. positional
# 2. keyword arguments(default value)
# 3. variable length   *args
# 4. variable length keyword arguments **kwargs

# add(1,4,5,2,5,23)
