def rotation():
    N=int(input("Enter the size of array"))
    D=int(input("Enter the size of rotation"))
    arr=[]

    for i in range(0, N):
        ele= int(input())
        arr.append(ele)
        arr1=arr
    for i in range(0, D):
        arr1= arr1[1:]
        arr1.append(arr[i])

    print(arr1)

T= int(input())
for i in range(0, T):
    rotation()
