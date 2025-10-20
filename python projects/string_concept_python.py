text="""
123 Python is an incredibly versatile programming language, first released in 1991. Its design philosophy emphasizes code readability with its notable use of significant whitespace. Many developers love Python for its simplicity and power. Whether you are working on web development, data science, or artificial intelligence,Python is a great choice. What will you build with it? For any questions, you can reach out to contact-us@example.com
"""

words=text.split(" ")
print(words)

print("\n ---words count>>>>>>>>>>\n")
print(len(words))


print("\n ---charater count method1>>>>>>>>>>>> \n")
c=0
for w in words:
    for i in w:
        c=c+1

print(f"method1 : total char count {c}")        

print("\n ---charater count method2>>>>>>>>>>>>> \n")
#sum of words :
total_char_count=sum(len(w) for w in words)
print(f"total char count:{total_char_count}")


print("\n ---charater wise count>>>>>>>>>>>>>>>\n ")   
c=0
for w in words:
    for i in w:
        c=c+1
    print(f"count of {i} is {c}")

print(type("abc"))
print(type(234))

for w in words:
    if type(w)=='int':
        print(w)
    elif type(w)=='str':
        print(w)
    else:
        print(f"{w} is : {type(w)}")


print("\n to find the mobile numner \n")

import re
text_with_numbers = """
You can contact support at 9876543210 for any help.
Another valid number is 8887776665. My account number is 123456789012345, which is not a mobile number.
You can also call +91-9998887776.
"""

pattern=r'\b(?:\+91-?)?(\d{10})\b'
mobile_number=re.findall(pattern,text_with_numbers)

if mobile_number:
    print(mobile_number)
else:
    print("not found mobile number")


# By using the regular expression how to find the vehicle number for example vehicle number is : RJ-05-AB-1234

# "Shuru mein 2 capital letters hote hain (State code)."
# "Fir ek hyphen (-) aata hai."
# "Fir 2 digits hote hain (RTO district code)."
# "Fir ek hyphen (-) aata hai."
# "Fir 2 capital letters hote hain (Vehicle series)."
# "Fir ek hyphen (-) aata hai."
# "Aakhir mein 4 digits hote hain (Unique number)."    

text = """
A car with number plate RJ-05-AB-1234 was seen.
Another car, DL-3C-AA-5678, was also there.
A truck with an old number, MH-12-A-987, passed by.
The correct format is UP-14-GH-5555.
"""

pattern=r'\b[A-Z]{2}-\d{2}-[A-Z]{2}-\d{4}'

vehicle_no=re.findall(pattern,text)
print(vehicle_no)




