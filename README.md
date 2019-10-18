# NameSort
This Python program reads names from a text file and sorts them first by length, then alphabetically.

Instructions for running NameSort on Windows: 

First, you must download a Python3.7 from the official website:
	https://www.python.org/ftp/python/3.7.4/python-3.7.4.exe

Afterwards, make sure you have both Sorting.py and a .txt file that you wish to sort. 
	** The text file should comtain names sepearated by a new line, i.e one name per line. **

Once both of these are ready, please do the following:
	- Open the command prompt.
	- Copy the Sorting.py file path and paste in in the command line, follow that with a space. 
	- Copy your .txt file's path, and paste it in the command line after the sorting.py file path.
		** It should look like <C:\Users\<user>(SORTING.PY FILE PATH) (.TXT FILE PATH) **
	- Hit enter.

The program will first output a list of names that are non-sortable, if there were any, for one of the following two reasons:
	1) The name began with a foriegn letter/character that was NOT one of 26 letters of the English Alphabet
	2) The name began with some punctuation mark, number, or any other character whose unicode value was not that of an English letter.

Then the program will output a list of names sorted by length, alphabetically. 
