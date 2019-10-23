import sys

if __name__ == "__main__":
    output = open(sys.argv[1])
    expected_output = open(sys.argv[2])

    output_list = output.readlines()
    expected_output_list = expected_output.readlines()

    got_error = 0

    for name in output_list:
        if output_list[name] != expected_output[name]:
            print("Error! Expected " + expected_output_list[name] + ", got " + output_list[name])
            got_error = 1

    if got_error == 0:
        print("No errors.")