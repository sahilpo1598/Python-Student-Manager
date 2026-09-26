'''
here i will use 
conditional- LOGIC
loops- MENU SYSTEM
dictionary- TO STORE DATA


in this project ..
1- ADD STUDENT
2- VIEW ALL STUDENT
3-CHECK RESULT
'''


STUDENT={}
while True:
    print("\n---student manager app--- ")
    print("1. add Student")
    print("2. view students")
    print("3. check result")
    print("4. Exit")

    choice = input("Enter your choice: ")
    if choice =="1":
        name = input("enter student name: ")
        marks= int(input("enter marks: "))
        STUDENT[name] = marks
        print(f"{name} successfully Added! ")
    elif choice == "2":
        if not STUDENT:
            print("No student found!")
        else:
            for name, marks in STUDENT.items():
                print(name,":", marks)
    elif choice == "3":
        name =input("enter the student name ")

        if name in STUDENT:
            marks = STUDENT[name]

            if marks >= 45:
                print("pass")
            else:
                print("fail")
                
    elif choice =="4":
        print("Exiting....")
        break
    else:
        print("in-valid input")








