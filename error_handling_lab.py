# Ask user for a filename
filename = input("Enter a filename to read (e.g., 'notes.txt'): ")

try:
    # Try to open and read the file
    with open(filename, 'r') as file:
        content = file.read()
    print("\nFile content:")
    print("-------------")
    print(content)
    print("-------------")

except FileNotFoundError:
    print(f"\nError: The file '{filename}' doesn't exist.")
except PermissionError:
    print(f"\nError: You don't have permission to read '{filename}'.")
except Exception as e:
    print(f"\nAn unexpected error occurred: {str(e)}")