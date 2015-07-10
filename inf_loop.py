x = range(10, 0, -1)
while True:
   print x
   line = raw_input('Enter a word: ')
   if line == 'done':
       break
print 'Sum: ' + str(sum(x)) + ' Count: ' + str(len(x)) + ' Ave: ' + str(sum(x)/len(x))
print 'Max: ' + str(max(x)) + ' Min: ' + str(min(x))

 
