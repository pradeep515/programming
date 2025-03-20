def inttoroman(num):
    roman_list = [
    [1000,"M"],
    [900,"CM"],
    [500,"D"],
    [400,"CD"],
    [100,"C"],
    [90,"XC"],
    [50,"L"],
    [40,"XL"],
    [10,"X"],
    [9,"IX"],
    [5,"V"],
    [4,"IV"],
    [1,"I"]
  ]
    result = '' 
    i = 0 
    while num > 0:
        for _ in range(num // roman_list[i][0]):
            result += roman_list[i][1]
            num -= roman_list[i][0]
            print(i)
        i += 1
    return result


if __name__ == '__main__':
    num = 3749
    print(inttoroman(num))