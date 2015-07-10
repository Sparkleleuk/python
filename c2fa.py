# Exercise temp try and except

Cel = raw_input('Enter temperature: ')
try: 
   fahr = float(Cel) * 9 / 5 + 32
   print fahr
except:
  print 'Please enter a number' 
