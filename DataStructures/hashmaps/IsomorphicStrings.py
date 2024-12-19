from collections import Counter

def isIsomorphic(s: str, t: str) -> bool:

    scounter = Counter(s)
    tcounter = Counter(t)

    print(scounter)
    print(tcounter)

    if len(s) != len(t):
        return False

    for i in range(len(s)):
        print(scounter[i])
        print(tcounter[i])
        if scounter[i] != tcounter[i]:
            return False
    return True


if __name__ == "__main__":
    str1 = "foo"
    str2 = "bar"
    print(isIsomorphic(str1, str2))