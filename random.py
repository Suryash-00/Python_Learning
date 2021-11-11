if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = str(input())
        score = float(input())

        students.append([name, score])

        list1 = []
        list2 = []

        for student in students:
            list1.append(student[1])

        for a in list1:
            if list1[a] > list1[a + 1]:
                temp = list1[a]
                list1[a] = list1[a + 1]
                list1[a + 1] = temp

        z = min(list1)

        while min(list1) == z:
            list1.remove(min(list1))

        for student in students:
            if student[1] == min(list1):
                list2.append(student[0])

        print(list2.sort())
