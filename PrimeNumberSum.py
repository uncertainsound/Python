# sieve to generate prime numbers
# generates list of prime numbers up to a limit, 
# finds the sum and tells the last prime number below the limit

import time


# Entering limit
valid_input = False                # switch to check for an integer
limit = raw_input("Enter Limit: ")
while valid_input == False:        #checking for an integer
  try:
    int(limit)
  except ValueError:               # if not, try again
    limit = raw_input("Not an integer.  Please enter an integer: ")
  else:
    limit = int(limit)             # convering limit to an integer
    valid_input = True             # breaking the while loop


#starting the timer
s = time.time()

# simplifying the calculation to speed it up
limitsqrt = int(limit**0.5) + 1
primelst = [2,3]
n = 5

# building the prime number list
while (n < limit):
  nsqrt = int(n**0.5) + 1
  for item in primelst:
    if (n % item == 0):
      isprime = False
      break
    else:
      isprime = True
    if (item > limitsqrt):
      break
  if isprime == True:
    primelst.append(n)
  n = n + 2              # checking only odd numbers

# finding the sum of the prime number list
total = 0
for items in primelst:
  total = total + items

# accounting for smaller numbers that don't work 
if limit == 4:
  total = 5
if limit == 3:
  total = 2
  primelst[-1] = 2
if limit < 3:
  total = 0
  primelst[-1] = "None"

# stopping the timer
time = time.time() - s
time = round(time, 2)

# display
print "Last prime below %s = %s" % (limit, primelst[-1])
print "Sum of primes below %s = %s" % (limit, total)
print "It took %s seconds to calculate this." % time


