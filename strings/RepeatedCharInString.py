#duplicate Characters 

str = "testpprogramming"
#method 1
counter = set()
for i in str:
    count = str.count(i)
    if(count >1):
        counter.add(i)
print (counter)


#method2
dict = {}
for i in str:
    if(dict.get(i) == None):
        dict[i] = "1"
    else:
        print(i + " a duplicate element")

