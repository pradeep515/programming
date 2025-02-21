from collections import Counter
def merge(strs):
        result = [] 
        result_dict = {}

        for str in strs:
            sorted_str = "".join(sorted(str))
            print(sorted_str)
            if sorted_str not in result_dict:
                result_dict[sorted_str] = [str]
            else:
                result_dict[sorted_str].append(str)
        print(result_dict)
        for _,value in result_dict.items():
            result.append(value)
        return result


if __name__=="__main__":

    strs = ["eat","tea","tan","ate","nat","bat"]
    print(merge(strs))