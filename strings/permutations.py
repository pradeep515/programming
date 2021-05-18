## print out all the permutations of given string.

def toString(List): ## just a utilty function to convert list to string
    return ''.join(List)

def permutate(name, l , r):
    if(l == r):
        print(toString(name))
    else:
        for i in range(l,r):
            name[i],name[l] = name[l],name[i]  #swap values . A-> A , A->B and fix for that 
            permutate(name, l+1, r)    # extend permutate to the remaining elements of the list.
            name[i],name[l] = name[l],name[i] #backtracking  .  return state to the original position.

if __name__ == '__main__':
    name = 'dory'
    list = list(name)
    permutate(list,0,len(list))