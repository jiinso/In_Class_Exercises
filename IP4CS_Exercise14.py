# jiinso
# 2014/11/11
# IP4CS
# Cellular Automata - Pascal's Triangle

# Choose a size for the 1-dimensional array, and create an array of zeros for that size.
size  = 225
listA = size*[0]
# Initial conditions: center value starts with 1
listA[(size-1)/2] = 1

# Define a function to update the single argument, listA
def Update(listA):
    n = len(listA)						# create an empty list (zeros) called newlist of the same size as listA
    newlist = n*[0]
    for i in range(0, n):					# for each of the cells in the list
    	if i == 0 or i == n-1:				# first and last cells are 0 (these do not change)
    	    newlist[i] = 0					
    	elif listA[i+1] == listA[i-1]:			# RULES FOR UPDATE from the original listA, if the cell's left and right neighbors are the same, 
    	    newlist[i] = 0					# the cell is updated to 0 in the newlist
        else:								# and if the cell's left and right neighbors are different values,
        	    newlist[i] = 1					# the cell is updated to 1 in the newlist
    return newlist						# return 

# Define a function to print out the list and it's updates as a changing pattern.
def PrintOut(listA):						
    print ''								# use a new line for each printout
    for each in listA:						# for each cell in listA
        if each == 1:						# use an asterisks to represent a 1
            print '*',
        else:								# use a blank to represent a 0
            print ' ',						# notice the comma after the print to keep the printing of the cells of one list on one single line.
    


# Main code
for i in range(size):						# for loop that prints out the same number of list updates as there are cells - this will create a squared printed pattern
    PrintOut(listA)						# print out listA
    listA = Update(listA)					# update listA
