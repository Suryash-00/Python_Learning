def sum(list):
    if list==[]:
        return 0
    else:
        return list[0]+sum(list[1:])

def count(list2):
    if list2==[]:
        return 0
    else:
        return 1+count(list[1:])