######### --- tuple practice---#############

# --- Concept 1: Tuple Banana (Creation & Packing) ---
# Hum app ki main configuration ko ek tuple mein pack kar rahe hain.
# (host, port, username, password)

df_config=("localhost",5432,"admin","admin123")
print(df_config)
print(type(df_config))

# concept 2: data access by indexing and slicing
print(df_config[0])  # localhost
print(df_config[1:3]) # (5432, 'admin')

# concept 3: Unpacking
host,port,username,password=df_config
print(host)      # localhost
print(port)      # 5432
print(username)  # admin
print(password)  # admin123

#concept 4: slicing
print(df_config[1:])  # (5432, 'admin', 'admin123')
print(df_config[:2])  # ('localhost', 5432)

print("\n **--- Example of tuple usage Route map ---**\n ")
#----------- IGNORE --- Project of road map

delhi_location=(28.7041,77.1025)
mumbai_location=(19.0760,72.8777)
kolkata_location=(22.5726,88.3639)
chennai_location=(13.0827,80.2707)

travel_route=[delhi_location,mumbai_location,kolkata_location,chennai_location]

print(travel_route)

for location in travel_route:
    print(location)
    print(f"Latitude: {location[0]}, Longitude: {location[1]}")

    if location[0]>20:
        print("Northern Hemisphere")
    else:
        print("Southern Hemisphere")    
        
print("\n **--- ----- To find the max, min, avg score by using tuple and unpacking concept\n ")            


def fun(scores):
    if not scores:
        return None,None,None
    else:
        min_score=min(scores)
        max_score=max(scores)
        avg_score=sum(scores)/len(scores)
        return min_score,max_score,avg_score
    

scores=[88,76,92,85,69,95,91]
min_s,max_s,avg_s=fun(scores)
print(f"min score:{min_s},max score:{max_s},avg_score:{avg_s}")

print("\n---------Project: Database Record Viewer--------\n")

# we usually see the rows of data in the form of tuples this is beacuse not changing data is more secure

employee_record=[(1,"John Doe","Engineer",75000),
                 (2,"Jane Smith","Manager",85000),
                 (3,"Sam Johnson","Analyst",65000) ]

for emp_id,name,position,salary in employee_record:
    print(f"ID:{emp_id},name : {name},Position:{position},salary:{salary}")

for record in employee_record:
    if record[3]>80000:
        print(f"high salary employee:{record[1]}")
    else:
        print(f"regular employee:{record[1]}")



