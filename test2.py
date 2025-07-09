def dividea(a,b):
    try:
        x=a/b
        return x
    except ZeroDivisionError:
        return "can't divide by zero"
a=int(input())
b=int(input())
print(dividea(a,b))
