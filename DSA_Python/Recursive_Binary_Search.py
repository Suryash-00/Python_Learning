def binary_Recursion(list, n, start, end):

    if start>end:
        return -1

    m=(start+end)/2

    if list[m]==n:
        return m

    if n<list[m]:
        return binary_Recursion(list, n, start, end-1)

    if n>list[m]:
        return binary_Recursion(list, n, start+1, end)

L=[2, 88, 99, 65]
binary_Recursion(L, 65, 0, 4)
