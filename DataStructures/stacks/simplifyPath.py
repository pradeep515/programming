
def simplifypath(s):
  
    componentlist = s.split('/')
    print(componentlist)

    result = []

    for component in componentlist:

        if component == '' or component == '.':
            continue
        elif component == "..":
                if result:
                    var = result.pop()
                    print(f"popped {var}")
        else:
            result.append(component)
    
    return '/' + '/'.join(result)


if __name__ == "__main__":
    s = "/home//foo/../Docs"
    # s = '/../'
    print(simplifypath(s))
