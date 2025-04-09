# Ask user for a filename (e.g., "poem.txt")
filename = input("Enter the filename to read: ")

try:
    # Read the original file
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Reverse each line and remove newline characters before reversing
    modified_lines = [line.rstrip('\n')[::-1] + '\n' for line in lines]

    # Create a new filename (e.g., "reversed_poem.txt")
    new_filename = "reversed_" + filename

    # Write to the new file
    with open(new_filename, 'w') as new_file:
        new_file.writelines(modified_lines)
    
    print(f"Success! Modified file saved as '{new_filename}'.")

except FileNotFoundError:
    print(f"Error: The file '{filename}' doesn't exist.")
except PermissionError:
    print(f"Error: You don't have permission to access '{filename}'.")
except Exception as e:
    print(f"An error occurred: {str(e)}")