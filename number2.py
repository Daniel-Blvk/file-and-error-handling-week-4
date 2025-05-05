input_file= input("Enter the name of the file to be opened: ")


try:

    with open(input_file, 'r') as file:
        contents = file.read()
        print(contents)

except FileNotFoundError:
    print(f"Error: The file '{input_file}' was not found.")
