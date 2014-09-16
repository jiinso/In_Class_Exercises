#In Class Exercise: Plotting graphs & Dictionaries
#9/11/2014

# Import needed functions.
import numpy as np
import pylab as pl
import string as str


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






#------------------------------------------------------------------------------------
#Exercise 2
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


code_in = raw_input('Type in the code you want to encode or decode. Watch the captalization: ')

code_out = ''
words = ''

letters = list(code_in)
print letters

for letter in letters:
	if letter == '!' or letter == '?':
	    code_out += letter
	    break
	code_out += encode_dict.get(letter)
	
print 
	
	    
	 