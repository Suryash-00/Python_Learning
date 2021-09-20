questions=open("D:\Python_Bootcamp\Files\questions.txt", "r")

question_list=[line.strip() for line in questions]
questions.close()

score=0
total=len(question_list)

for line in question_list:
    q,a=line.split("=")
    ans=input(f"{q}=")
    if a==ans:
        score+=1
    
result=open("result.txt", "w")
result.write(f"Your final score is {score}/{total}.")
result.close()