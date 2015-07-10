# Exercise grading system 

score = raw_input('Enter your score:   ')
if float(score) >= 0.9:
   print 'A'
elif float(score) >= 0.8:
   print 'B' 
elif float(score) >= 0.7:
   print 'C' 
elif float(score) >= 0.6:
   print 'D' 
elif float(score) < 0.6:
   print 'F'


def computegrade (score):
   if score > 0.9:
      print 'A'
   elif score < 0.9:
      print 'B'

grade = computegrade (0.1)



