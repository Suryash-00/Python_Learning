#friend= 'Suri'
#user_name= input("Enter your name")
#if user_name==friend:
#    print("He is friend")
#else:
#    print("He is stranger")

friends= ['Daksh', 'Yash', 'Vivek']
family= ['Vaibhav', 'Suman', 'Shammi']
user_name= input("Enter your name")
if user_name in friends:
    print("Hello! Friend")
elif user_name in family:
    print("Hello! Family")
else:
    print("We don't know you!")    