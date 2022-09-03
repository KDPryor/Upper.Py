#upper.py ver. 1.2 by Ken Pryor 09/02/2022
#Accepts input of lower/mixed case text,
#converts it to uppercase & sends output
#clipboard for easy pasting to other app.

import pyperclip as pc

text = input('What do you wish to convert?\n')

uppercase = text.upper()
pc.copy(uppercase)

print('Your text is now in the clipboard. Do you wish to me to place it in a text file for you?\n')

answer1 = input('Y or N\n')

if answer1 == 'y':
	f=open("output.txt", "a+")
	for i in range(1):
		f.write(uppercase)
		f.write('\n')
	f.close()
else: print('bye')