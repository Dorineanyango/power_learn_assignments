# File Read & Write Challenge 
def modify_file():
    try:
        # Read content from the original file
        with open("source.txt", "r") as file:
            content = file.readlines()

        # Modify the content (e.g., make all text uppercase)
        modified_content = [line.upper() for line in content]

        # Write modified content to a new file
        with open("modified_output.txt", "w") as file:
            file.writelines(modified_content)

        print("Modified content has been saved to 'modified_output.txt'.")
    
    except FileNotFoundError:
        print("The file 'source.txt' was not found.")
    except IOError:
        print("There was an error reading or writing the file.")


# Error Handling Lab 
def safe_file_read():
    filename = input("Enter the filename you want to read: ")
    
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("\nFile Content:\n")
            print(content)
    
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except PermissionError:
        print(f"You don't have permission to read the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the functions to test them
modify_file()
safe_file_read()
