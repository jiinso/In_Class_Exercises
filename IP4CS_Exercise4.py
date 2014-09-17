#In Class Exercise: Plotting graphs & Dictionaries
#9/11/2014


# Import needed functions.
import numpy as np
import pylab as pl



# Exercise 1

# Part 1
x = np.linspace(0.100,10)
y = x**3 - 2*x - 6

pl.figure(1)
pl.plot(x,y)
pl.xlabel('x')
pl.ylabel('y')
pl.title('[Exercise 1] Part 1: Graph of Equation')
pl.show()


# Part 2
pl.figure(2)
data = np.loadtxt('stars.txt', float)
x2 = data[:,0]
y2 = data[:,1]
pl.scatter(x2,y2)
pl.xlabel('x')
pl.ylabel('y')
pl.title('[Exercise 1] Part 2: Stars Scatter Plot')
pl.show()


# Part 3
pl.figure(3)
data_density = np.loadtxt('circular.txt', float)
pl.imshow(data_density)
pl.xlabel('x')
pl.ylabel('y')
pl.title('[Exercise 1] Part 3: Circular Density Plot')
pl.show()






#------------------------------------------------------------------------------------------------------------------------------------------------------------
#Exercise 2

# import the function sleep from package time to delay the process of reading through the script.
from time import sleep

# create a dictionary that has the keys set to the decoding set.
encode_dict = {
    'a':'n',
    'b':'o',
    'c':'p',
    'd':'q',
    'e':'r',
    'f':'s',
    'g':'t',
    'h':'u',
    'i':'v',
    'j':'w',
    'k':'x',
    'l':'y',
    'm':'z',
    'n':'a',
    'o':'b',
    'p':'c',
    'q':'d',
    'r':'e',
    's':'f',
    't':'g',
    'u':'h',
    'v':'i',
    'w':'j',
    'x':'k',
    'y':'l',
    'z':'m',
    'A':'N',
    'B':'O',
    'C':'P',
    'D':'Q',
    'E':'R',
    'F':'S',
    'G':'T',
    'H':'U',
    'I':'V',
    'J':'W',
    'K':'X',
    'L':'Y',
    'M':'Z',
    'N':'A',
    'O':'B',
    'P':'C',
    'Q':'D',
    'R':'E',
    'S':'F',
    'T':'G',
    'U':'H',
    'V':'I',
    'W':'J',
    'X':'K',
    'Y':'L',
    'Z':'M',
}


code_in = raw_input('Welcome to Caesar cipher! Please type in the code you want to encode or decode. Watch the captalization: ')

code_out = ''
words = ''

letters = list(code_in)

for c in letters:
	if c == '!' or c == '?' or c == '.' :
	    code_out += c
	elif c == ' ':
	    code_out += ' ' 
	else:
	    code_out += encode_dict.get(c)

print 'Encoding/decoding. Please wait a few seconds....'
sleep (5)
print code_out

	
	    
	 