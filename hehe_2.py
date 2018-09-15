info = {}
name = input("please enter your name:")
age = int(input("please enter your age:"))
info["name"] = name
info["age"] = age

# for i in info.items():
#     print(i)
#
# print('finish!')

# for k,v in info.items():
#     print(k,v)

# for k,v in info.items():
#     print("%s--->%s" %(k,v))

for k,v in info.items():
    print(k + ":" ,v)







