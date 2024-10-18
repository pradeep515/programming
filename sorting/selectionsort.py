# slection sort
selection = [1,68,6,4,44,777,88,45,11]

# 1 - loop through the elements an find the minimum number . 
# @ - Swap the mimimum element to the front. 
# 3 - Then repeat the same leaving the first element
size = len(selection)
for i in range(size):
    minindex = i
    for j in range(i+1,size):#we can take i+1 as starting point, since we set minindex to i in the first run. So we can compare it with i+1 and so on
        if selection[j]< selection[minindex]:
            minindex = j 
    selection[i], selection[minindex] = selection[minindex], selection[i]
print (selection)
