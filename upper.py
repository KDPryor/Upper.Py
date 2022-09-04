#upper.py ver. 1.3 by Ken Pryor 09/02/2022
#Accepts input of lower/mixed case text, converts it to uppercase & sends output
#to the clipboard. Offers to output to a text file as well.

import pyperclip as pc

text = input('What do you wish to convert?\r\n')

uppercase = text.upper()
pc.copy(uppercase)

print('Your text is now in the clipboard. Do you wish to me to place it in a text file for you?\n')

answer1 = input('Y or N\r\n')
answer1 = answer1.lower()

if answer1 == 'y':
	f=open("output.txt", "a+")
	for i in range(1):
		f.write(uppercase)
		f.write('\n')
	f.close()
else: print('bye')
