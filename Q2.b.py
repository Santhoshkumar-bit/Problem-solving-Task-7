import datetime

def create_timestamp_file():
    # Get the current timestamp
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Define the filename
    filename = "timestamp_file.txt"
    
    # Open the file in write mode
    with open(filename, 'w') as file:
        # Write the current timestamp to the file
        file.write(f"Current timestamp: {timestamp}")
    
    print(f"File '{filename}' created with timestamp.")

# Execute the function
if __name__ == "__main__":
    create_timestamp_file()
