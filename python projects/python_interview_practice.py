# Swap two numbers without using a third variable
a=1
b=2
a,b=b,a
print(a,b)

# Reverse a string
s="pritam"
print(s[::-1])

#Count vowels in a string
s = "I love Python"
vowels = "aeiouAEIOU"

print(sum(1 for ch in s if ch in vowels))

#Add all numbers in a list
lst=[1,2,3,4]
print(sum(lst))

#Find max and min from a list
lst1=[1,2,4,7,8,3,2]
print(max(lst1))
print(min(lst1))

#Convert a list to a tuple
lst=[1,2,3]
print(tuple(lst))

#Remove duplicates using a set
numbers = [1, 2, 2, 3, 3, 4, 4, 5]
print(list(set(numbers)))

#Merge two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
print({**dict1,**dict2})

#Get keys and values from a dictionary
student = {"name": "Karan", "age": 22, "marks": 88}
for k,v in student.items():
    print(k,v)

#Find length of each data type
x = "Python"
y = [1, 2, 3, 4]
z = {"a": 10, "b": 20}
print(len(x),len(y),len(z))

#Create a set from a string
str1="preetam"
print(set(str1))

#Multiple assignment in one line
x,y,z=5,10.5,"python"
print(x,y,z)

#Nested list se sab numbers ka sum nikalo
nums = [[1, 2, 3], [4, 5], [6, 7, 8]]
lst4=[]
for sublist in nums:
    lst4.extend(sublist)
print(sum(lst4))    

#Nested list se sab numbers ka sum nikalo using list comprehension
print([i for sublist in nums for i in sublist])


#Dictionary me highest value ka key find karo
scores = {"A": 45, "B": 67, "C": 89, "D": 55,"E":10}
max_val=max(scores,key=scores.get)
print(max_val)

#Merge list of dictionaries
data = [{"a": 1}, {"b": 2}, {"c": 3}]
merge={}
for d in data:
    merge.update(d)
print(merge)


#Find common elements from two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1&set2)

#Find unique words in a sentence
sentence = "python is great and python is easy"
words=set(sentence.split())
print(words)

sentence = "python is great and python is fun"
remove_dup_words=[]
for i in sentence.split():
    if i not in remove_dup_words:
        remove_dup_words.append(i)
print(remove_dup_words) 

#Dictionary comprehension for square of numbers
sq={x:x**2 for x in range(1,6)}
print(sq)

#List comprehension for square of numbers
for i in range(1,6):
    print(f"{i}:{i**2}")

#List of tuples → Dictionary
pairs=[("a", 10), ("b", 20), ("c", 30)]
print(dict(pairs))

#Convert dictionary → list of keys and values
person = {"name": "Karan", "age": 25, "city": "Delhi"}
for k,v in person.items():
    print(f"key:{k} value:{v}")

keys=list(person.keys())
values=list(person.values())
print(f"keys : {keys} values:{values}")

#Remove all duplicates from list but preserve order
nums = [1, 2, 2, 3, 1, 4, 5, 4]
print(list(set(nums)))

#Remove all duplicates from list but preserve order without using set
unique_lst=[]
for i in nums:
    if i not in unique_lst:
        unique_lst.append(i)
    else:
        pass    

print(unique_lst)    

#Find all even numbers in nested list
nums = [[1, 2, 3], [4, 5, 6], [7, 8]]
flatten1=[]
for sublist in nums:
    for i in sublist:
        flatten1.append(i)
even=[i for i in flatten1 if i%2==0]
print(flatten1)
print(even)

#Find all even numbers in nested list in simple way
nums = [[1, 2, 3], [4, 5, 6], [7, 8]]
even_using_lc=[i for sublist in nums for i in sublist if i%2==0]
print(even_using_lc)

#Reverse dictionary (keys → values, values → keys)
d = {"a": 1, "b": 2, "c": 3}
keys=list(d.keys())
values=list(d.values())
print(keys,values)
print(dict(zip(values,keys)))

#Reverse dictionary (keys → values, values → keys) using dict comprehension
d = {"a": 1, "b": 2, "c": 3}
reversed_dict={v:k for k,v in d.items()}
print(reversed_dict)


#Sort dictionary by values
data = {"apple": 3, "banana": 1, "cherry": 2}
sorted_dict=sorted(data.items(),key=lambda x:x[1])
print(sorted_dict)

#Find frequency of each character
s = "banana"
u_s=list(set(s))
for i in u_s:
    c=0
    for j in s:
        if i==j:
            c=c+1
    print(f"{i}: {c}")

#Find frequency of each character using get:
s = "banana"     
freq={}
for ch in s:
    freq[ch]=freq.get(ch,0)+1
print(freq)          

#Nested dictionary traversal
students = {
    "Karan": {"Math": 85, "Science": 90},
    "Riya": {"Math": 95, "Science": 80}
}
for name, subjects in students.items():
    for sub, marks in subjects.items():
        print(name, sub, marks)

#Check mutable vs immutable
x = [1, 2, 3]
y = x
y.append(4)
print(x)

a = "hello"
b = a
b += " world"
print(a)


#Find the length of a string without using len()
str1="pritam"
c=0
for ch in str1:
    c=c+1
print(c)    

#Replace all vowels with ‘*’
s = "Education"
vowels = "aeiouAEIOU"

new_s=""
for ch in s:
    if ch in vowels:
        new_s=new_s+"*"
    else:
        new_s=new_s+ch

print(new_s)            

#Find the first non-repeated character
s = "aabbcde"
u_str=list(set(s))
freq={}
for ch in s:
    freq[ch]=freq.get(ch,0)+1

print(freq)   

for k,v in freq.items():
    if v==1:
        print(k)
        break

#Find the first non-repeated character using count function:
s = "aabbcde"
print(s.count("a"))
for ch in s:
    if s.count(ch)==1:
        print(ch)
        break

#Check if string contains only digits
s = "12345"
if s.isdigit():
    print("yes only digits")
else:
    print("no digits")    

#Swap case (upper → lower, lower → upper)
s = "PyThOn"
print(s.swapcase())

#Remove duplicate characters
s = "programming"
print("".join(list(set(s))))

#Remove duplicate characters preserve the order
s = "programming"
r_s=""
for ch in s:
    if ch not in r_s:
        r_s=r_s+ch

print(r_s)

#Check if two strings are anagrams Anagram = same letters but different order.
s1 = "listen"
s2 = "silent"

if sorted(s1)==sorted(s2):
    print("anagram")
else:
    print("not anagram")    

#Reverse each word in a sentence
s = "I love Python"
words=s.split()
rev_words=[w[::-1] for w in words]
print(" ".join(rev_words))

#Remove all special characters
s = "P@y#th$o%n!"
clean=""

for ch in s:
    if ch.isalnum():
        clean=clean+ch
print(clean)        

#Count uppercase, lowercase, digits & special chars
s = "PyThon123$#"
upper = lower = digit = special = 0

for ch in s:
    if ch.isupper():
        upper=upper+1
    
    elif ch.islower():
        lower+=1
    elif ch.isdigit():
        digit+=1
    else:
        special+=1

print(upper,lower,digit,special)

# Find the most frequent character
#method 1:
s = "success"

for ch in s:
    print(f"{ch} : {s.count(ch)}")

freq={}
for ch in s:
    freq[ch]=freq.get(ch,0)+1
print(freq)

print([k for k,v in freq.items() if v>1])

#method 2:
max_char=max(s,key=s.count)
print(max_char)

#Capitalize first letter of every word (without using title())
s = "python is fun"
words=s.split()
print(" ".join(w[0].upper()+w[1:] for w in words))


#Remove characters at even indexes
s = "abcdefg"
n=[]
for i in range(len(s)):
    if i%2!=0:
        n.append(s[i])

print("".join(n))

#Find common characters between two strings
s1 = "apple"
s2 = "grape"
comman=set(s1)&set(s2)
print(comman)

#Find ASCII value of each character
s="abc"
for ch in s:
    print(ord(ch))


#Convert alternate characters to uppercase
s = "python"
alt_st=""
for i in range(len(s)):
    if  i%2==0:
        alt_st+=s[i].upper()
    else:
        alt_st+=s[i].lower()
print(alt_st)     

#Check if a string contains all unique characters
s = "python"
if len(s)==len(set(s)):
    print("all unique")
else:
    print("not unique")    
  
#Find the longest word in a sentence
s = "Python is a powerful programming language"
words=s.split()
len_of_w=[len(w) for w in words]
print(max(len_of_w))


#Count uppercase letters without using isupper()
s = "PyThon"
c=0
for ch in s:
    if ch.isupper():
        c=c+1
print(c)      

#Replace digits with their word form
s = "I have 2 apples and 3 bananas"
words = {'0':'zero','1':'one','2':'two','3':'three','4':'four',
         '5':'five','6':'six','7':'seven','8':'eight','9':'nine'}

words_s=""
for ch in s:
    if ch.isdigit():
        words_s+=words[ch]
    else:
        words_s+=ch

print(words_s)        

#Find second most frequent character
def find_second_most_frequent_manual(text):
    """
    Finds the second most frequent character using a manual dictionary.
    """
    if not text:
        return None
        
    # 1. Count frequencies manually
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    
    # 2. Sort the counts
    # We sort the items (key-value pairs) based on the value (count)
    # 'key=lambda item: item[1]' tells sort to look at the count
    sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    
    # sorted_counts for "hello world" will be:
    # [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]
    
    # 3. Check if there is a second item
    if len(sorted_counts) < 2:
        return None

    # 4. Get the character from the second item
    # sorted_counts[1] is ('o', 2)
    # sorted_counts[1][0] is 'o'
    return sorted_counts[1][0]

# --- Example ---
my_string = "programming"
second_char = find_second_most_frequent_manual(my_string)
print(f"\nString: '{my_string}'")
print(f"Second most frequent character: '{second_char}'") # 'r', 'g', 'm' are all 2


# First non repeating character 
str1="aabbccde"
freq={}
for ch in str1:
    freq[ch]=freq.get(ch,0)+1

print(freq)
lst=[k for k,v in freq.items() if v==1]
print(lst[0])


s = "aabbccde"
for ch in s:
    if s.count(ch) == 1:
        print(ch)
        break

#sliding window sum
lst=[1,2,3,4,5,6]
k=3
new_lst=[]
for i in range(len(lst)-k+1):
    window_sum=sum(lst[i:i+k])
    new_lst.append(window_sum)

print(new_lst)   


#Function with default argument
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Priya")

#*args — Variable Number of Arguments *args tab use hota hai jab aapko pehle se nahi pata kitne arguments function me pass honge.
#Yeh sab arguments ko ek tuple me store karta hai.
def total_bill(*prices):
    return sum(prices)

print(total_bill(100, 200, 50))     # 3 items
print(total_bill(500, 120, 230, 150))  # 4 items

#Real-Life Example 2: Logging or Debugging Tool helps jab message me unpredictable text add karna ho.
def log_message(*args):
    print("[LOG]:", *args)

log_message("Error:", "Invalid password", "at", "login()")


#**kwargs — Keyword Arguments **kwargs tab use hota hai jab function ko key-value pairs me flexible arguments milte hain.
#Yeh sab ko ek dictionary me store karta hai.

def make_api_call(**params):
    print("API called with:", params)

make_api_call(url="https://api.example.com", method="GET", timeout=5)
make_api_call(url="https://geeksforgeeks",ipaddress="172.34.5.90")

#Real-Life Example: Using Both Together

def generate_report(*args,**kwargs):
    print("student details",kwargs.get("name"))
    print("subjects",args)

generate_report("math","science","hindi",name="pritam",age=23)

#Lambda ek small anonymous function hoti hai — matlab naam nahi hota (no def keyword).
#. lambda arguments: expression
#1. Example 1: Function returning a lambda
sq=lambda x:x*x
print(sq(5))

#2. Using Lambda with Built-in Functions Lambda is most useful with Python’s higher-order functions like map(), filter(), and sorted().

nums=[1,2,3,4,5]
print(list(map(lambda x:x**2,nums)))


print(list(filter(lambda x:x%2==0,nums)))

students = [("Amit", 90), ("Riya", 85), ("Karan", 95)]

print(sorted(students,key=lambda x:x[0]))


#lambda for one line 
print((lambda x,y:x+y)(4,5))

#Maximum of two numbers
max_no=lambda a,b :a if a>b else b
print(max_no(2,10))

#first latter capital
names = ["rahul", "priya", "amit"]
print(list(map(lambda n:n.capitalize(),names)))


format_list=lambda lst: list(map(lambda n:n[0].upper()+n[1:].lower(),lst))
print(format_list(names))

#without using the map function how to use list in lambda function: Another example — Square every number
lst=[1,2,3,4,5,6]

fun=lambda lst:[x**2 for x in lst]
print(fun(lst))


# try and except
try :
    print(1/0)
except Exception as e:
    print(e) 

try:
    f=open("text.txt","r")
    print(f.read())
 
except Exception as e1:
    print(e1)      

#Write a program to create a text file and write some lines in it.

with open("text.txt","w") as f:
    f.write("hello this is line 1 \n")
    f.write("hello this is line 2 \n")

print("File sucessfully written")

#Read the file content and display it.

with open("text.txt","r") as f:
    content=f.read()

print("file content is below\n",content)    

#Read a file line by line using a loop.
with open("text.txt","r") as f:
    for line in f:
        print(line.strip())

#Append new text to an existing file.
with open("text.txt","a") as f:
    f.write("this is new line which has been added\n")

print("new line is added successfully")

#Count how many lines, words, and characters are in a file.
with open("text.txt","r") as f:
    lines=f.readlines()

num_lines=len(lines)
num_words= sum(len(line.split()) for line in lines)   
num_chars=sum(len(line) for line in lines) 
print(num_lines)
print(num_words)
print(num_chars)

#Copy content of one file into another.
with open("text.txt","r") as src:
    with open("dest.txt","w") as dest:
        dest.write(src.read())

print("files copy sucessfully")    

with open("dest.txt","r") as f:
    print(f.read())

#Read a file and print only the lines that contain a specific word (e.g., “hello”).
word="hello"
with open("text.txt","r") as f:
    for line in f:
        if word in line:
            print(line.strip())    

#Handle file not found error using try-except.
try:
    with open("missing.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)     

#Replace a specific word in a file (without losing content)
with open("text.txt","r") as f:
    data=f.read()

data=data.replace("hello","pri")
with open("text.txt","w") as f:
    f.write(data)

print("write data successfully!")

with open("text.txt","r") as f:
    print(f.read())

#Write a list of strings to a file (each item in a new line)
list1=["apple","orange","mango"]

with open("fruits.txt","w") as f:
    for item in list1:
        f.write(item+"\n")

with open("fruits.txt","r") as f:
    print(f.read())        


#create a new text file 
print("################This is the new files and project\n")
with open("python.txt","w") as f:
    f.write("Python is easy to learn.\n")
    f.write("Practice makes you perfect.\n")
    f.write("Keep learning every day.\n")



with open("python.txt","r") as f:
    content=f.read()   
    print(content) 
  
#count the lines in file:
with open("python.txt","r") as f:
    c=0
    for line in f:
        if "Python" in line:
            c=c+1
    print(c)        
        
#Ignore Comment Lines (starting with ‘#’)
with open("python.txt","r") as f:
    c=0
    for line in f:
        if not line.strip().startswith("#"):
            c=c+1
    print(c)  

#Write Only Unique Names to a New File
with open("python.txt","r") as f:
    names=f.read().splitlines()
    print(names)

unique_names=list(set([item for sublist in set(names) for item in sublist.split()]))

print(unique_names)

with open("uniquenames.txt","w") as f:
    for name in unique_names:
        f.write(name+" ")   

with open("uniquenames.txt","r") as f:
    print(f.read())