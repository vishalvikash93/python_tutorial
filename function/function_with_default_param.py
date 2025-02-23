def greet(name="Guest",lname="",address=""):
    print(f"Hello, {name}!")


def greet1(**kwargs):
    print(f"kwargs type, {type(kwargs)}!")
    print(f"kwargs, {kwargs}!")
    if kwargs.get('fname'):
        print(f'fname:{kwargs.get('fname')}')
    if kwargs.get('lname'):
        print(f'lname:{kwargs.get('lname')}')
# Calling the function with a value
# greet("Alice")  # Output: Hello, Alice!
#
# # Calling the function without a value
# greet()  # Output: Hello, Guest!

greet1(fname="shruti",lname="babu",address="")