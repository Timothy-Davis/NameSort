import sys


def sort_names(name_list):
    # This list will contain all the names whose first character falls outside of the English alphabet.
    nonsortable_name_list = []

    index = 0
    while index < len(name_list):

        # First, strip extra characters (such as \n and spaces) off of each item in the list. This isolates the name.
        name_list[index] = name_list[index].strip()

        # If stripping the spaces and \n's from an entry leaves an empty string, we can remove it from the list.
        if name_list[index] == '':
            name_list.remove(name_list[index])

            # If we do remove an entry from the list we can't increment index or else we'll skip next element
            index -= 1

        # If the first character of a name falls out of the ASCII range for English letters, we cannot sort the name.
        elif ord((name_list[index])[0]) < 65 or ord((name_list[index])[0]) > 122:
            nonsortable_name_list.append(name_list[index])
            name_list.remove(name_list[index])

            # Since we remove the item from the name list, we need to make sure index doesn't increment.
            index -= 1

        # increment index to keep the loop moving forward
        index += 1

    # Now that pre-requisites are taken care of, we can sort the list by length alphabetically
    name_list.sort(key=lambda x: (len(x), x))

    # If our list of non-sortable names has any values, we'll print it out as well.
    if len(nonsortable_name_list) != 0:
        print("The following names are not sortable: ", end='')
        print(nonsortable_name_list)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("There are too few arguments! Please pass a text file to sort.")
        sys.exit()
    elif len(sys.argv) > 2:
        print("There are too many arguments, assuming the first argument: ")
    name_file = open(sys.argv[1], "r", encoding='utf-8')
    name_list = name_file.readlines();

    sort_names(name_list)
    for name in name_list:
        print(name)
