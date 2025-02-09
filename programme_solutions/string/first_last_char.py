input_string = input("Enter the string: ")

if input_string[0].lower() == input_string[-1].lower():
    print("The first and last characters are the same.")
else:
    print("The first and last characters are not the same.")
