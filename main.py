"""
@author allen
@version 1.0 file created
@date May/06/2019
"""
import sys

"""

Fn = Fn-1 + Fn-2
where, F0 = 0; F1 = 1

"""
# previous term, initial term in formula is always 0
f_previous = 0
# starting term, first term is in the formula always 1
f_current = 1
# list of the fibonacci terms
fibonacci_sequence = []
# index of arguments
index = 0
# list of arguments
arguments = sys.argv[2:]

# iterates through until it reaches the integer inputted in the console
for index in range(int(sys.argv[1])):
    fibonacci_sequence.append(str(f_previous))
    # prints out the current Fibonacci term
    print("F-{}:\t{}".format(index, f_previous))
    # calculates the next Fibonacci terms
    f_previous, f_current = f_current, f_previous + f_current

# output the file in the local folder since there was no
if len(arguments) == 1:
    # opens the output text file
    fw = open('fibonacci_output.txt', 'w')
    # checks for the correct argument
    if arguments[0] == "-o":
        # iterates through each element in the fibonacci list adding a newline after each insertion
        for element in fibonacci_sequence:
            fw.write(element)
            fw.write("\n")
    # closes the file to save memory
    fw.close()

else:
    # opens the output text file at the specified filepath
    fw = open((arguments[1] + 'fibonacci_output.txt'), 'w')
    # checks for the correct argument
    if arguments[0] == "-o":
        # iterates through each element in the fibonacci list adding a newline after each insertion
        for element in fibonacci_sequence:
            fw.write(element)
            fw.write("\n")
    # closes the file to save memory
    fw.close()
