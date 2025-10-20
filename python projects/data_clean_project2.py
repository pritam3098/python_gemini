# # Python mein "Array" (yaani List)
# Python mein, jab hum "array" bolte hain, to aam taur par hamara matlab list se hota hai. Doosri languages (jaise C++ ya Java) ke array se Python ki list zyada flexible hoti hai.

# Traditional Array: Ek hi type ka data rakhta hai (sirf numbers ya sirf strings).

# Python list: Alag-alag type ka data ek saath rakh sakti hai (numbers, strings, etc.).




# # ## map() Function ka Jaadu ✨
# # map() function ek bahut hi powerful tool hai. Iska kaam hai ek function ko lena aur use ek list (ya doosre iterable) ke har ek item par apply kar dena.

# # Syntax: map(function, iterable)

# # function: Woh kaam jo aap har item par karna chahte hain.

# # iterable: Aapki list, jiske items par kaam karna hai.

# # numbers=[1,2,3,4,5]

# # def squ_fun(n):
# #     return n*n

# # square_of_nums=list(map(squ_fun,numbers))
# # print(f"square number by using the map function : {square_of_nums}")



# ###########Project of using map , list , set and dictionary#######

# # Our raw data is in a LIST of strings
# raw_product_data = [
#     "  APPLE iPhone 15 (Blue) - 79900 ",
#     "SAMSUNG Galaxy S24 (Gray) - 74999   ",
#     "  apple Macbook Air M3 - 114900",
#     "samsung Galaxy Book4 - 65990",
#     "      APPLE iPhone 15 (Blue) - 90000"
# ]

# cleaned_list=[]

# for i in raw_product_data:
#     cleaned_list.append(i.strip().split(" - "))

# print(f"cleaned list :{cleaned_list}")

# print("---------------------------------------------------")

# dict1={}
# for i in cleaned_list:
#     k,v =i
#     dict1[k]=int(v)
# print(f"dict1 : {dict1}")

# set_items=set(dict1.items())
# print(set_items)


# print("---------------------------------------------------")
   
# product_list=[] 
# for k in dict1.keys():
#     product_list.append(k)

# print(f"product_list : {product_list}")

# product_price=[]

# for v in dict1.values():
#     product_price.append(v)

# print(f"product_price : {product_price}")    


# print("---------------------------------------------------")
# # Raw data: A list of dictionaries
# student_data = [
#     {
#         'name': 'Aisha',
#         'scores': ['88', '92', '80']  # Notice scores are strings
#     },
#     {
#         'name': 'Ben',
#         'scores': ['65', '70', '68']
#     },
#     {
#         'name': 'Chris',
#         'scores': ['95', '89', '91']
#     }
# ]
# # name=[]
# # score=[]

# # for s in student_data:
# #     name.append(s['name'])
# #     score.append(s['scores'])

# # print(f"student name : {name}")
# # print(f"student score : {score}")        

# # int_score=[]
# # for sublist in score:
# #     new_sublist=[]
# #     for item in sublist:
# #         new_sublist.append(int(item))

# #     int_score.append(new_sublist)

# # print(f"int_score: {int_score}")

# # new_dict=dict(zip(name,int_score))
# # print(f" create new dict:{new_dict}")

# # avg_score=[]
# # for l in int_score:
# #         avg_score.append(round(sum(l)/len(l),2))
# # print(f"avg score : {avg_score}")    

# # avg_dict_create=dict(zip(name,avg_score))
# # print(f"avg dict created : {avg_dict_create}")


# print("\n--- by using the map function---\n")
# student_data = [
#     {
#         'name': 'Aisha',
#         'scores': ['88', '92', '80']  # Notice scores are strings
#     },
#     {
#         'name': 'Ben',
#         'scores': ['65', '70', '68']
#     },
#     {
#         'name': 'Chris',
#         'scores': ['95', '89', '91']
#     }
# ]

# student_name=[]
# student_score=[]
# for student in student_data:
#      student_name.append(student['name'])
#      student_score.append(student['scores'])

# print(f"student names:{student_name}")
# print(f"student score:{student_score}")


# student_score_int=[]
# for score_list in student_score:
#     student_score_int.append(list(map(int,score_list)))

# print(f"student score in int : {student_score_int}")


######################################## Use of Map function

# numbers = [1, 2, 3, 4, 5]

# # A function that squares a number
# # def square(n):
# #     return n * n

# # Use map() to apply the 'square' function to each item in 'numbers'

# # IMPORTANT: map() returns a map object (an iterator), not a list.
# # We need to convert it to a list to see the results.

# print(f"Using map(): {list(map(lambda num:num*num,numbers))}")


############################# Project of cleaning the raw dicitionary

# Raw product data for a cleaning exercise
raw_product_data = [
    {
        'product_id': 'P001',
        'product_name': 'Wireless Mouse',
        'category': 'Electronics',
        'price': '₹1,299.00',
        'stock_quantity': 150,
        'rating': 4.5,
        'dimensions_cm': '10x6x4'
    },
    {
        'product_id': 'P002',
        'product_name': 'USB-C Cable',
        'category': 'electronics',
        'price': '₹499',
        'stock_quantity': 300,
        'rating': 4.7,
        'dimensions_cm': '100x1x1'
    },
    {
        'product_id': 'P003',
        'product_name': 'Mens Cotton T-Shirt',
        'category': 'Apparel',
        'price': '₹850.50',
        'stock_quantity': 500,
        'rating': 4.2,
        'dimensions_cm': None
    },
    {
        'product_id': 'P004',
        'product_name': 'Coffee Mug',
        'category': 'Home & Kitchen',
        'price': '₹399.00',
        'stock_quantity': 0,
        'rating': None,
        'dimensions_cm': '12x9x9'
    },
    {
        'product_id': 'P001',
        'product_name': 'Wireless Mouse',
        'category': 'Electronics',
        'price': '₹1,299.00',
        'stock_quantity': 150,
        'rating': 4.5,
        'dimensions_cm': '10x6x4'
    },
    {
        'product_id': 'P005',
        'product_name': 'Notebook Diary',
        'category': 'Stationery',
        'price': '250',
        'stock_quantity': 1000,
        'rating': 4.9,
        'dimensions_cm': '20x15x2'
    }
]


product_id_list=[]
price_list=[]
stock_quantity_list=[]
rating_list=[]
dimensions_cm_list=[]

for p in raw_product_data:
    product_id_list.append(p['product_id'])
    price_list.append(p['price'])
    stock_quantity_list.append(p['stock_quantity'])
    rating_list.append(p['rating'])
    dimensions_cm_list.append(p['dimensions_cm'])


   


stock_quantity_list_update=[True if s>0 else False for s in stock_quantity_list]
print(f"stock_quantity_list_update : {stock_quantity_list_update}")

price_list_updated=[p if '₹' in p else f"{"₹"}{p}" for p in price_list]
print(f"price_list_updated : {price_list_updated}")

rating_list_updated=["invalid" if r is None else r for r in rating_list]

len_cm=[]
width_cm=[]
height_cm=[]

list_of_sublist=[]
for list1 in dimensions_cm_list:
    if list1 is not None:
        list_of_sublist.append(list1.split('x'))
    else:
        list_of_sublist.append("invalid")    

print(f"sublist : {list_of_sublist}")   


for sublist in list_of_sublist:
    if sublist!='invalid':
        len_cm.append(sublist[0])
        width_cm.append(sublist[1])
        height_cm.append(sublist[2])



product_id_list_unique=list(set(product_id_list))


print(f"product_id_list : {product_id_list}")
print(f"price_list : {price_list}")
print(f"stock_quantity_list : {stock_quantity_list}")
print(f"rating_list : {rating_list}")
print(f"dimensions_cm_list : {dimensions_cm_list}")
     
print("\n ---------------- \n")

print(f"product id list : {product_id_list_unique}")
print(f"price_list:{price_list_updated}")
print(f"stock_quantity_list:{stock_quantity_list_update}")
print(f"rating_list_updated: {rating_list_updated}")
print(f"length : {len_cm} , width : {width_cm}, height : {height_cm}")


print("\n ---------------- \n")
keys=['product_id','price','stock quantity','rating','lenth','width','height']
list_of_dict=[]
for student_data_tuple in zip(product_id_list_unique,price_list_updated,stock_quantity_list_update,rating_list_updated,len_cm,width_cm,height_cm):
    list_of_dict.append(dict((zip(keys,student_data_tuple))))

print(list_of_dict)







