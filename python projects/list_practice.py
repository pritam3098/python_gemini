# tasks=[]
# while True:
#     print(" please choose :")
#     print("1. Add new task")
#     print("2. Delete task")
#     print("3. Show task")
#     print("4. Exit")

#     choice=int(input("enter the choice :"))

#     if choice==1:
#         task=input("Add new task: ")
#         tasks.append(task)
#         print(tasks)

#     elif choice==3:
#         if not tasks:
#             print("nothing in the task list kindly add!")
#         else:
#             for i,task in enumerate(tasks,start=1):
#                 print(f"index : {i} and task : {task}")


#     elif choice==2: 
#         del_task=int(input("enter the task you to delete"))   

#         print(tasks.pop(del_task-1))


#     elif choice==4:
#         print("Exit!")
#         break  
#     else:
#         print("invalid")  
    
        
# append(item)	Aakhir mein ek item jodna.
# insert(index, item)	Beech mein kahin item jodna.
# extend(list2)	Ek list mein doosri list ke saare items jodna.
# remove(item)	Naam se item hatana.
# pop(index)	Position se item hatana.
# sort() Items ko order mein lagana (A-Z, 0-9).
# reverse()	List ko ulta karna.
# len(list)	List ki total lambai batana.
##




## list comprehesion

fruites=['apple','banana','grapes']

fruits_with_a_char=[c.upper() for c in fruites if 'n' in c]
print(fruits_with_a_char)

