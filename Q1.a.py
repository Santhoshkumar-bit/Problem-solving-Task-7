import datetime

def create_test_file():
    # Get the current timestamp
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Create a filename with the timestamp
    filename = f"test_file_{timestamp}.txt"
    print(filename)
    
    # Open the file in write mode
    with open(filename, 'w') as file:
        file.write("This is a test file created on " + timestamp)
    
    print(f"File '{filename}' created successfully.")

# Call the function to create the test file
create_test_file()
