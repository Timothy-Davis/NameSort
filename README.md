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

# NameSortUT (Unit Test)
The following are instructions for running the Name Sort Unit Test program.

Please note the following:
	- The path to your Sorting.py file, noted in the README as ProgramPath
	- The path to your input text file, noted in the README as InputPath
	- The path to your NameSortUT.py file, noted in the README as UTPath
	- The path to your expected output text file, noted in the README as ExpectedOutputPath
	- The path to the included UnitTesting.bat file, noted in the README as TestingPath

Edit the included batch file, making the following changes:

	- In the line under the first REM, type the following:
		ProgramPath "InputPath"

	- In the line under the second REM, type the following
		UTPath .\sorted_names.txt ExpectedOutputPath
		
Open the Windows command prompt and type the following:
	TestingPath

If the output is anything other than "No errors." then there are one of three issues:

	1) The names aren't the same in both text files; this would mean that
	   there is an issue with the sorting algorithm that is causing the names
	   to be sorted in the wrong order.*

	2) There are more names in the sorted_names file than the expected output file;
	   this would either mean that names are being added the input file unneseccarily,
	   OR that the expected output file is incorrect.**

	3) There are more names in the expected output file than the sorted_names file;
	   this would either mean that names are being removed from the input file unneseccarily,
	   OR that the expected output file is incorrect.**
	
	* You will know because the program will output the name it expected vs the name it recieved.
	** You will know becasuse you will get an "Index out of bounds" exception.
