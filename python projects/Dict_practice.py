# ############# Add dictionay word ##########

translator={}
print("1. Add new word")
print("2. show all words")
print("3. delete a word")
print("4. Exit")

while True:
    choice=int(input("enter the choice: "))
    if choice==1:
        english_word=input("enter the english word :")
        hindi_word=input(f"enter the hindi meaning of {english_word}")
        translator[english_word]=hindi_word
        print(f"hindi translation of {english_word} has been added successfully")

    elif choice==2:
        for k,v in translator.items():
            print(f"{k}:{v}")

    elif choice==3:
        del_word=input("enter the word you want to delete :")
        if del_word in translator:
            del translator[del_word]
            print(f"{del_word} has been deleted successfully!")
        else:
            print("delete word not found")    

    elif choice==4:
        print("exit")
        break

    
########## word frequecy counter ##############

text="hello hello everyone this is very nice day can we meet again"
words=text.lower().split()
print(words)

word_counts={}
for w in words:
    word_counts[w]=word_counts.get(w,0)+1

for w in word_counts.keys():
    print(f"{w}")

for w,c in word_counts.items():
    print(f"{w} :{c}")


###### how to delete values #######

# 1. create a dictionary
dict_example={}

while True:
    key=input("enter the key")
    if key!='done':
        value=input(f"enter the value of {key}: ")
        dict_example[key]=value
        print(dict_example)
    else:
        print("done")
        break 

for k,v in dict_example.items():
    print(f"{k}:{v}")

#simple deletion 
del_key=input("enter the key you want to delete:")
if del_key in dict_example:
    del dict_example[del_key]
    print(f"delete the {del_key} successfully!")

print(dict_example)

#return value and del the key
del_key_return_value=input("enter the key you want to delete:")
if del_key_return_value in dict_example:
    val=dict_example.pop(del_key_return_value)
    print(f"deleted key value is {val}")

print(dict_example)
#delete last item

del_last_item=input("enter the key you want to delete:")
if del_last_item in dict_example:
    dict_example.popitem()
    print("deleted item which is last inserted")










  






    
    


