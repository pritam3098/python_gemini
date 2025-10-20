# # Raw customer data for a cleaning exercise 1
# Is Data mein Cleaning ke Tasks
# Yahan ek checklist hai ki aapko is data mein kya-kya theek karna hai:

# Full Name ko Saaf karna:

# Shuru aur aakhir ke extra spaces hatayein.

# Prefixes jaise 'Mr.' ko hatayein.

# Extra info jaise '(old)' ko hatayein.

# Challenge: Kya aap full_name se first_name aur last_name ke do alag columns bana sakte hain?

# Phone Numbers ko Standardize karna:

# Phone numbers alag-alag formats mein hain. Sabko ek standard format mein laayein (jaise 1234567890).

# Special characters jaise (, ), -, +91- hatayein.

# 'N/A' jaisi entries ko handle karein (shayad None ya khaali chhod dein).

# Email ko Validate aur Clean karna:

# Extra spaces hatayein.

# Sabhi emails ko lowercase mein convert karein taaki consistency bani rahe.

# Gair-valid email (jaise 'mohan@example') ko pehchanein.

# Dates ko Theek karna:

# registration_date alag-alag formats (YYYY-MM-DD, DD/MM/YYYY, DD-Mon-YYYY) mein hai. Sabko ek standard datetime format mein convert karein.

# Login Details ko Parse karna:

# last_login_details ek string hai jismein IP address aur Device dono hain.

# Is ek column se do naye columns (ip_address aur device_type) banayein.

# Missing value (None) ko handle karein.


raw_customer_data = [
    {
        'customer_id': 101,
        'full_name': '  Mr. Arun Kumar ',
        'email': 'arun.kumar@example.com ',
        'phone_number': '(123) 456-7890',
        'registration_date': '2024-01-15',
        'last_login_details': 'IP: 192.168.1.1, Device: Desktop'
    },
    {
        'customer_id': 102,
        'full_name': 'Priya Sharma',
        'email': 'PRIYA.SHARMA@EXAMPLE.COM',
        'phone_number': '9876543210',
        'registration_date': '20/02/2024',
        'last_login_details': 'IP: 192.168.1.2, Device: Mobile'
    },
    {
        'customer_id': 103,
        'full_name': 'Mohan Singh (old)',
        'email': 'mohan@example',
        'phone_number': 'N/A',
        'registration_date': '2023-11-30',
        'last_login_details': 'IP: 192.168.1.3, Device: Tablet'
    },
    {
        'customer_id': 104,
        'full_name': 'Sunita Devi',
        'email': ' sunita.d@example.com',
        'phone_number': '+91-8877665544',
        'registration_date': '10-Mar-2024',
        'last_login_details': 'IP: 192.168.1.4, Device: Mobile'
    },
    {
        'customer_id': 105,
        'full_name': 'Ravi Verma',
        'email': 'ravi.v@example.com',
        'phone_number': '7766554433',
        'registration_date': '2024-04-05',
        'last_login_details': None
    }
]


full_name_list=[]
email_list=[]
phone_number_list=[]
registration_date_list=[]
last_login_details_list=[]

for customer in raw_customer_data:
    full_name_list.append(customer['full_name'].lower().replace('(old)',"").replace('mr.',"").strip().split())
    email_list.append(customer['email'].lower().strip())
    phone_number_list.append(customer['phone_number'].replace('-',"").replace('(',"").replace(') ',"")\
                             .replace('-',"").replace('+91-',"").replace('+91','').replace('N/A',"").strip())
    registration_date_list.append(customer['registration_date'])
    last_login_details_list.append(customer['last_login_details'])

print(f"full_name_list : {full_name_list}")    
print(f"email_list: {email_list}")   
print(f"phone_number_list : {phone_number_list}")   
print(f"registration_date_list: {registration_date_list}")   
print(f"last_login_details_list: {last_login_details_list}")   

print("\n -------------- \n")

firstname=[]
lastname=[]
for i in full_name_list:
    firstname.append(i[0])
    lastname.append(i[1])

print(f"first name : {firstname}")
print(f"lastname : {lastname}")    

from datetime import datetime

def convert(d_str):

    possible_formats = [
        "%Y-%m-%d",      # e.g., 2025-10-12
        "%d/%m/%Y",      # e.g., 12/10/2025
        "%b %d, %Y",     # e.g., Oct 12, 2025
        "%Y.%m.%d" ,      # e.g., 2025.10.13
        "%d-%b-%Y"
    ]

    for fmt in possible_formats:
        try:
            date_obj=datetime.strptime(d_str,fmt)
            return date_obj.strftime("%Y-%m-%d")
        except ValueError:
            pass
    return None 
   
std_dates_list=[]
for d_str in registration_date_list:
    std_dates_list.append(convert(d_str))


print(f"std_date_list : {std_dates_list}")    

list_of_lists=[]      
for i in last_login_details_list:
    if i is not None:
        list_of_lists.append(i.split(","))
    else:
        None    

print(list_of_lists)        

ip_value_extract=[]
device_value_extract=[]

for sublist in list_of_lists:
    ip_value_extract.append(sublist[0].split("IP:"))
    device_value_extract.append(sublist[1].split("Device:"))

ip_value=[i[1] for i in ip_value_extract]
device_value=[i[1] for i in device_value_extract]

print(f"ip value : {ip_value}")
print(f"device value:{device_value}") 

print("\n -------------- \n")

keys=['firstname','lastname','dates','ip_value','device_value']
cleaned_dict=[]
for customer_tuple_value in zip(firstname,lastname,std_dates_list,ip_value,device_value):
    cleaned_dict.append(dict(zip(keys,customer_tuple_value)))

print(cleaned_dict)

