def binary_recursion(array, n, start, end):

    if start>end:
        return -1

    m=(start+end)//2

    if array[m]==n:
        print(m)
        return m

    if n<array[m]:
        return binary_recursion(array, n, start, m-1)

    if n>array[m]:
        return binary_recursion(array, n, m+1, end)

L=[2, 65, 88, 99]
binary_recursion(L, 99, 0, 3)
