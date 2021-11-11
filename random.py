arr=[]
n = int(input("Enter subjects"))
for i in range(0, n):
    ele = int(input("Enter marks"))
    arr.append(ele)
for i in range(0, n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

while n != 0:
    i = 1
    n = n - 1
    if arr[n - i] < arr[n]:
        print(arr[n - i])
        break
