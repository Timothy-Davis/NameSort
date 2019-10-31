@echo off
"../Sorting.py" "../Sort Me.txt" "asc" > output_asc.txt
NameSortUT.py output_asc.txt Expected_Output_Asc.txt

"../Sorting.py" "../Sort Me.txt" "desc" > output_desc.txt
NameSortUT.py output_desc.txt Expected_Output_desc.txt