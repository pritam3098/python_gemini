# # import re
# # s=input()
# # s=re.sub(r'[^a-z0-9]','',s.lower())
# # print(s==s[::-1])

# # m=[[1,2,3],[4,5,6]]
# # print(list(zip(*m)))

# # import random
# # names=input("names :").split()
# # random.shuffle(names)
# # print("team:",names[:2])

# # print("-".join(names))

# # n=int(input("num:"))
# # f=1
# # for i in range(1,n+1): f*=i
# # print("fact: ",f)

# import time
# print("work for 5 sec")
# time.sleep(5)
# print("break time")

import time,random
for i in range(1,100):
    print(f"Hacking ....{i}%",end="\r") #\r use krne pr hm ek hi line me overwrite kr skte hai 
    time.sleep(random.uniform(0.01,0.05))

print("\n Hack complete!")    