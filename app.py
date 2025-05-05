def modify_file(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                outfile.write(line)
        print(f"Successfully copied '{input_file}' to '{output_file}'")
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
   

if __name__ == "__main__":
    input_file = input("Enter the name of the input file: ")
    output_file = input("Enter the name of the output file: ")
    modify_file(input_file, output_file)

    # try using different files or the files in the folder