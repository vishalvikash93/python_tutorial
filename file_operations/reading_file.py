# Opening a file in read mode
with open('problem.txt', 'r') as file:
    content = file.readlines()
    print(content)
    for i in content:
        print(i)


# file_obj=open('problem.txt',)
# print(file_obj.read())
# # file_obj.write("Hi")
# file_obj.close()

# with open('/home/vishal/Downloads/techVision/python_tutorial/problem.txt','r+') as f:
#     # f.write("Hi i am learner")
#     content=f.readlines()
#     for line in content:
#         print(line)
