from sys import argv
import re

scriptname, filename = argv

number_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

total_count = 0
non_number = 0


print ""
print "Opening: ", filename
print "--------------------"
datastore = open(filename, 'r').read()

data = datastore.split()

print " "
print "Enhancing..."
print "------------"
print " "

# if the first charater of the contents of the array slot is = 1, then...

for number in data:
    if re.match("^.", number) == 1:
        number_count[1] += 1
        total_count += 1 

# Note that 2-9 are relics, the previous implementation was to .list() everything, then count individual numbers. But, Benfords law applies only to the First number, so 101 counts a one '1', not two.
    elif number == '2':  
        number_count[2] += 1 
        total_count += 1 
    elif number == '3':
        number_count[3] += 1 
        total_count += 1 
    elif number == '4':
        number_count[4] += 1 
        total_count += 1 
    elif number == '5':
        number_count[5] += 1 
        total_count += 1 
    elif number == '6':
        number_count[6] += 1 
        total_count += 1 
    elif number == '7':
        number_count[7] += 1
        total_count += 1 
    elif number == '8':
        number_count[8] += 1 
        total_count += 1 
    elif number == '9':
        number_count[9] += 1  
        total_count += 1 
    else:
        non_number += 1

b_count = [0, total_count * .3, total_count * .18, total_count * .12, total_count * .10, total_count * .08, total_count * .07, total_count * .06, total_count * .05, total_count * .04]

number_diff = [0, abs(b_count[1] - number_count[1]), abs(b_count[2] - number_count[2]), abs(b_count[3] - number_count[3]), abs(b_count[4] - number_count[4]), abs(b_count[5] - number_count[5]), abs(b_count[6] - number_count[6]), abs(b_count[7] - number_count[7]), abs(b_count[8] - number_count[8]), abs(b_count[9] - number_count[9])]

  
total_diff = number_diff[1] + number_diff[2] + number_diff[3] + number_diff[4] + number_diff[5] + number_diff[6] + number_diff[7] + number_diff[8] + number_diff[9]

print "Printing Results:"
print "-----------------"
print "You had %d 1's (expecting: %d, difference: %d)" % (number_count[1], b_count[1], number_diff[1])
print "You had %d 2's (expecting: %d, difference: %d)" % (number_count[2], b_count[2], number_diff[2])
print "You had %d 3's (expecting: %d, difference: %d)" % (number_count[3], b_count[3], number_diff[3])
print "You had %d 4's (expecting: %d, difference: %d)" % (number_count[4], b_count[4], number_diff[4])
print "You had %d 5's (expecting: %d, difference: %d)" % (number_count[5], b_count[5], number_diff[5])
print "You had %d 6's (expecting: %d, difference: %d)" % (number_count[6], b_count[6], number_diff[6])
print "You had %d 7's (expecting: %d, difference: %d)" % (number_count[7], b_count[7], number_diff[7])
print "You had %d 8's (expecting: %d, difference: %d)" % (number_count[8], b_count[8], number_diff[8])
print "You had %d 9's (expecting: %d, difference: %d)" % (number_count[9], b_count[9], number_diff[9])
print "You had %d characters that weren't numbers." % non_number
print " "
print "Total difference: %d" % total_diff

percent_diff = (total_diff / total_count) * 100

print "Percent difference: %d" % percent_diff
print " "
print "----------"
print "CONCLUSION"
print "----------"
print " "
if percent_diff <= 10:
    print "Your total variation from our projected values was less than or equal to 10%, this document is PROBABLY LEGIT."
elif percent_diff > 10 and percent_diff <= 30: 
    print "Your total variation from our projected values was greater than 10%, but less than our equal to 30, this document is QUESTIONABLE."
elif percent_diff > 30:
    print "Your total variation from our projected values was greater than 30%, this document is FALSIFIED!"
else:
    print "It appears we've got a non numeric answer from our calculations... our bad."
