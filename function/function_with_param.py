from operator import length_hint


def add(a, b):
    sum = a + b
    # mul=a*b
    # return sum,mul
    return sum


def test(a,b,*args,**kwargs):
    print(f'args type:{type(args)}')
    print(f'args values :{args}')
    print(f'a:{a}')
    print(f'b:{b}')
    print(kwargs)

test(2,5,2,5,7,24,53.29,90,fname="suman",lname="kumari")

# res = add(1, 4)
# print(res)
# Calling the function
# sum_result = add(5, 3)
# print(sum_result)  # Output: 8
# print(type(sum_result))


# 1. positional
# 2. keyword arguments(default value)
# 3. variable length   *args
# 4. variable length keyword arguments **kwargs

# add(1,4,5,2,5,23)
