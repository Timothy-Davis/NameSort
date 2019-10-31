# NameSort
This Python program reads names from a text file and sorts them first by length (ascending or descending), then alphabetically.

Instructions for running NameSort on Windows: 

First, you must download a Python3.7 from the official website:

	https://www.python.org/ftp/python/3.7.4/python-3.7.4.exe

Afterwards, navigate to the NameSort directory.

Once both of these are ready, please do the following:

	If you want the list sorting by length ascending, type:
		Sorting.py "Sort Me.txt" asc
	If you want the list sorted by length descending, type:
		Sorting.py "Sort Me.txt" desc

The program will first output a list of names that are non-sortable, if there were any, for one of the following two reasons:

	1) The name began with a foriegn letter/character that was NOT one of 26 letters of the English Alphabet
	2) The name began with some punctuation mark, number, or any other character whose unicode 
	   value was not that of an English letter.

Then the program will output a list of names sorted by length, alphabetically. 

# NameSort Unit Test
The following are instructions for running the Name Sort Unit Test program.

First, navigate to the 'Testing' directory.
Once there, type the following command to run the test:

	UnitTesting.bat

If the output is anything other than than two "No errors." then there is one of three issues:

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
