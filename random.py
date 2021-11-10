def runner_up():
    arr=[]
    n = int(input("Enter subjects"))
    for i in range(0, n):
        ele = int(input("Enter marks"))
        arr.append(ele)
    print(arr)

    for i in range(n):
        for j in range(n):
            if arr[j] < arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp

    for i in range(0, n):
        print(arr[i])

    i = 1
    while n != 0:
        i = i + 1
        n = n - 1
        if arr[n - i] < arr[n - 1]:
            print(arr[n - i])

runner_up()