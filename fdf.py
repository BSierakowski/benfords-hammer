from sys import argv

scriptname, filename = argv

# Array to hold the number of 1's, 2's, 3's, etc. 
# Array[0] left in so that we can reference number_count[1] to tell us how many numbers started with 1.
number_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Total numbers counted
total_count = 0

# Container for anything that isn't a number
non_number = 0

print ""
print "Opening: ", filename
print "--------------------"

# Loading in the file
datastore = open(filename, 'r').read()

# Splitting the file, so that '100 100 200' will give us ['100', '100', '200']
data = datastore.split()

# Most important step, always enhance.
print " "
print "Enhancing..."
print "------------"
print " "

# Declaring an array for later use
datalist = []

# For loop to run through the previously split data and list it, so that 
# ['100', '100', '200'] gives us [['1','0','0'],['1','0','0'],['2','0','0']]
for i in data:
    datalist.append(list(i))
    
# Here's where the magic happens, now that each word has been split and each letter of the split word has been
# listed, we run a for loop through our listed array, and look at the first element of the array 'number[0]'
# and see if its a 1, 2, 3, etc. This isolates the first charater of every word, and increments counts as needed.
for number in datalist:
    if number[0] == '1':
        number_count[1] += 1
        total_count += 1 
    elif number[0] == '2':
        number_count[2] += 1 
        total_count += 1 
    elif number[0] == '3':
        number_count[3] += 1 
        total_count += 1 
    elif number[0] == '4':
        number_count[4] += 1 
        total_count += 1 
    elif number[0] == '5':
        number_count[5] += 1 
        total_count += 1 
    elif number[0] == '6':
        number_count[6] += 1 
        total_count += 1 
    elif number[0] == '7':
        number_count[7] += 1
        total_count += 1 
    elif number[0] == '8':
        number_count[8] += 1 
        total_count += 1 
    elif number[0] == '9':
        number_count[9] += 1  
        total_count += 1 
    else:
        non_number += 1

# The mysterious b_count! What does it do?! I stated above that the for loop was the magic, A MERE DIVERSION!!
# b_count uses benford's law to look at the total number of numbers, and then create a value in the array to represent
# what it should be. EG, 30% of the numbers should be 1, so b_count[1] gives you 30% of the total numbers. 
# Again, b_count[0] left in place so that b_count[5] equals the expected number of 5's.
b_count = [0, total_count * .3, total_count * .18, total_count * .12, total_count * .10, total_count * .08, total_count * .07, total_count * .06, total_count * .05, total_count * .04]

# Math! Calculates the difference (in absolute value) between what the expected number is (b_count) and what the number
# actually was. If there are 100 numbers, we expect thirty 1's, if there were actually twenty nine 1's, our number_diff[1] = 1
number_diff = [0, abs(b_count[1] - number_count[1]), abs(b_count[2] - number_count[2]), abs(b_count[3] - number_count[3]), abs(b_count[4] - number_count[4]), abs(b_count[5] - number_count[5]), abs(b_count[6] - number_count[6]), abs(b_count[7] - number_count[7]), abs(b_count[8] - number_count[8]), abs(b_count[9] - number_count[9])]

# Total difference in all numbers, how far off is it? Used to calculate "total offness(tm)"
total_diff = number_diff[1] + number_diff[2] + number_diff[3] + number_diff[4] + number_diff[5] + number_diff[6] + number_diff[7] + number_diff[8] + number_diff[9]


# Printing the results, number of 1's counted, number of 1's expected, and the absolute difference between the two.
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

# Error check to prevent dividing by 0 (ie, ending universe.) You're welcome.
if total_count == 0:
    total_count += 1

# Calculating the % difference between what's expected and what the document has.
percent_diff = (total_diff / total_count) * 100

# Final conclusion output, with 3 tiers based on how far off it is.
print "Percent difference: %d" % percent_diff
print " "
print "----------"
print "CONCLUSION"
print "----------"
print " "
if percent_diff <= 10:
    print "Your total variation from our projected values was less than or equal to 10%, this document is PROBABLY LEGIT."
    print "(meaning 'legitly random.')"
    print "  "
elif percent_diff > 10 and percent_diff <= 30: 
    print "Your total variation from our projected values was greater than 10%, but less than our equal to 30, this document is QUESTIONABLE."
    print "(meaning likely to have had systematic or human intervention.)"
    print "  "
elif percent_diff > 30:
    print "Your total variation from our projected values was greater than 30%, this document is FALSIFIED!"
    print "(meaning not random, changed by a human or other logic based system.)"
    print "  "
else:
    print "It appears we've got a non numeric answer from our calculations... our bad."
    print "  "
