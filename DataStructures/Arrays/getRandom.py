import random 

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.nums_dict = {}

    def insert(self, val: int) -> bool:
        if val not in self.nums_dict:
            self.nums.append(val)
            index = len(self.nums)-1
            self.nums_dict[val] = index
            return True
        else:
            return False


    def remove(self, val: int) -> bool:
        if val in self.nums_dict:
            index = self.nums_dict[val]
            last_elval = self.nums[-1]
            self.nums[index] = last_elval
            self.nums_dict[last_elval] = index 
            self.nums.pop()
            del self.nums_dict[val]
            
            return True
        else:
            return False
        
    def getRandom(self) -> int:
        return random.choice(self.nums)

if __name__ == "__main__":
    obj = RandomizedSet()
# ["RandomizedSet","remove","remove","insert","getRandom","remove","insert"]
# [[],[0],[0],[0],[],[0],[0]]
    print(obj.remove(0))
    print(obj.remove(0))
    print(obj.insert(0))
    print(obj.nums)
    print(obj.nums_dict)
    print(obj.getRandom())
    print(obj.remove(0))
    print(obj.nums)
    print(obj.nums_dict)
    print(obj.insert(0))
  
