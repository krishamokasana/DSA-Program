def operation(a,b):
    """sum=a+b
    sub=a-b
    div=a/b
    mul=a*b
    return sum,sub,div,mul"""
    return a+b,a-b,a/b,a*b

x=int(input("enter x="))
y=int(input("enter y="))
sum,sub,div,mul = operation(x,y)
print("Sum=",sum)
print("Sub=",sub)
print("Div=",div)
print("Mul=",mul)
#print("resunt=",operation(x,y))
