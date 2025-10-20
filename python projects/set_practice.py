python_student_list=set(["Pritam","Ankit","Rohit","Sagar","Aman"])
datascience_student_list=set(["Pritam","Ankit","Rohit","Sagar","Aman","Nikhil","Rakesh"])


# concept 1: common students in both the list
common_students=python_student_list.intersection(datascience_student_list)
print("common students in both the list:",common_students)

# concept 2: all the students in both the list
all_students=python_student_list.union(datascience_student_list)
print("all the students in both the list:",all_students)    

# concept 3: students only in python list
only_python_students=python_student_list.difference(datascience_student_list)
print("students only in python list:",only_python_students)

# concept 4: students only in datascience list
only_datascience_students=datascience_student_list.difference(python_student_list)
print("students only in datascience list:",only_datascience_students)


print("shopping list example-----")
shopping_list=set()
while True:
    print(" please choose :") 
    print("1. Add new item")
    print("2. Delete item")
    print("3. Show item")
    print("4. Exit")

    choice=int(input("enter the choice :"))

    if choice==1:   
        item=input("Add new item: ")
        shopping_list.add(item)
    elif choice==2: 
        del_item=input("enter the item you to delete")   
        shopping_list.discard(del_item)
    elif choice==3:
        if not shopping_list:
            print("nothing in the shopping list kindly add!")
        else:
            for i,item in enumerate(shopping_list,start=1):
                print(f"index : {i} and item : {item}")
    else:
        print("Exit!")
        break


    
                
