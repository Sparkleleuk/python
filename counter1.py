# Exercise 6.3: Counter function 

def counter(w):
   count = 0  
   for char in w:
      if char == '3':
         count = count + 1

   return count     
            
w = raw_input('Enter data: ')
print counter(w)
 
