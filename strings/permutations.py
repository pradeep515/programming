## print out all the permutations of given string.


def permutate(name, l , r):
    if(l == r):
        print(list)
    else:
        for i in range(l,r):
            name[i],name[l] = name[l],name[i]
            permutate(name, l+1, r)
            name[i],name[l] = name[l],name[i] #backtracking

if __name__ == '__main__':
    name = 'dory'
    list = list(name)
    permutate(list,0,len(list))