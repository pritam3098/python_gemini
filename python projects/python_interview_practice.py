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

#Dictionary comprehension for square of numbers
sq={x:x**2 for x in range(1,6)}
print(sq)

#List comprehension for square of numbers
sq_lst=[x**2 for x in range(1,6)]
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



    
