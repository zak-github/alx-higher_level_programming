def safe_print_list(my_list=[], x=0):
    # Initialize a variable to keep track of the number of elements printed
    elements_printed = 0

    # Use a for loop to iterate through the list
    for element in my_list:
        try:
            # Try to print the element
            print(element, end=" ")
            elements_printed += 1
        except:
            # If an exception occurs (e.g., when the element is not printable), continue to the next element
            continue

        # Check if we have printed 'x' elements, if so, break the loop
        if elements_printed >= x > 0:
            break

    # Print a newline character to end the line
    print()

    # Return the real number of elements printed
sh: 1: q: not found
