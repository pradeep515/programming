
def leftrotation(s,d):
     leftroatationstring = s[d:]+s[:d]
     rightrotatedstring = s[-d:]+s[:-d]
     print(leftroatationstring)
     print(rightrotatedstring)

          


if __name__ == "__main__":
     name = 'pradeep'
     leftrotation(name,4)