def countdown(i):
    print(i)

    if i<=0:
        return None
    else:
        countdown(i-1)

countdown(5)

def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)

fact(5)