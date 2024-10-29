
def sqrt(num):
   if  num == 0 or num ==1:
      return num
   else:
      for i in range(2, num):
         if i*i > num:
            return i-1

   

 


    
if __name__ == "__main__":
   print(sqrt(200))



 

