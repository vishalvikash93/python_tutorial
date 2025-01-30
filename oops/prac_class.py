class calculator:
    # def __init__(self,param1,param2):
    #     self.x=param1
    #     self.y=param2

    def addition(self,*args):
        temp=0
        for i in args:
            temp+=i
            pass
        return temp


calc=calculator()
res=calc.addition(10,20,40,34)

print(f'res:{res}')