
student_db=[]

def add_student():
    roll_no=int(input("enter the roll no:"))
    name=input("enter the name :")
    contact_info=input("enter the contact info:")
    stud_records={
        'roll_no':roll_no,
        'name':name,
        'contact_info':contact_info
    }
    student_db.append(stud_records)
    return student_db

def delete_student(del_roll_no,student_db):
    new_database=[s for s in student_db if s['roll_no']!=del_roll_no]
    return new_database 


def show_student():
    for s in student_db:
        print(f"roll no :{s['roll_no']}, name : {s['name']}, contact_info : {s['contact_info']}")

while True:
    print(" 1. Add details")
    print(" 2. delete the details")
    print(" 3. show the details")

    choice=int(input("enter the choice :"))
    if choice==1:
        print(add_student())
    elif choice==2:
        del_roll_no=int(input("enter the value you want to delete: "))
        print(delete_student(del_roll_no,student_db))
    elif choice==3:
        show_student() 
    else:
        print("exit")





