def read_file(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Read the content of the file
            content = file.read()
            
        # Display the content
        print(content)
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    
    except IOError:
        print(f"Error: An I/O error occurred while trying to read '{filename}'.")

# Example usage
if __name__ == "__main__":
    # Replace 'example.txt' with your actual file name
    read_file('example.txt')
