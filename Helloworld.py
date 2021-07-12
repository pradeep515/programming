# # print ('hello world')

# s = "I am good man"
# print(s.count('o'))
# print(s[::-1])
# print(len(s))
# #tuple\
# tup = ("can", "apples", "bananas")
# print(tup)
# #dictionary 
# dict1 = {"pradeep": 32, "sreekanth": 45}
# print(dict1["sreekanth"])
# del dict1["sreekanth"]
# print(dict1)
# #Set
# fruitsset = {"apples", "mangoes", "apples"}
# fruitsset.add("grapes")
# print(fruitsset)

# #for
# listtest = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,23232]
# print(max(listtest))


# #class
# class Car:
#     def __init__ (self, color, size):
#         self.color= color
#         self.size= size
#     def getcolor(self):
#         print(self.color)
#         print(self.size)

# c1 = Car("blue", 44)
# c1.getcolor()

# newset = {"pradeep","sreekanth"}
# newset.add("radhika")
# newset.add("pradeep1")
# print(sorted(newset))
# print(newset)

#dict update
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({'year':5959})
# print(thisdict)
# print(thisdict.get("brand"))
# print(thisdict.keys())
# print(thisdict.values())
# print(thisdict.items())
# for x in thisdict:
    # print x


# list = []
# list.append("sreekanth")
# print(list)
# list.append("pradeep")
# # print(list)
# print(list.pop(0))
# print list

# name = "pradeep"
# nameagedict = {1:"pradeep", 2: "sreekanth", 3:"greg"}
# print(len(nameagedict))
# for x in nameagedict:
#     if nameagedict[x]==name:
#         print("the name is already there")
#         break
#     else:
#         print("the name is not there")

# countdict = {}
# name = "pradeep"
# for i in name:
#     if(i in countdict):
#         countdict[i] = countdict.get(i)+1
#     else:
#         countdict[i] = 1
# print(countdict.items())

list = [3,4,3,5,3,4,6,7]
countdict = {}
for i in list:
    if i in countdict:
        countdict[i] = countdict.get(i) +1
    else:
        countdict[i] = 1

maxvalue = 0
maxkey = 0
for key,value in countdict.items():
    if value > maxvalue:
        maxvalue = value
        maxkey = key 
# print(maxkey)
i = 0
j = 0
for number in list:
    if maxkey == number:
        j = j + 1
        i = j
    else:
        j = j + 1
print i




     








