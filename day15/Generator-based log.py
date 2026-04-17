# Generator function to read file line by line
def read_logs(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                yield line.strip()   # return one line at a time
    except FileNotFoundError:
        print("File not found!")


# Dictionary to store error counts
error_count = {}

# Process logs
for log in read_logs("log.txt"):
    
    # Condition: check if line contains ERROR
    if "ERROR" in log:
        
        # Extract error message (example: after ERROR)
        parts = log.split("ERROR")
        if len(parts) > 1:
            error_msg = parts[1].strip()
            
            # Count occurrences using dictionary
            if error_msg in error_count:
                error_count[error_msg] += 1
            else:
                error_count[error_msg] = 1


# Print results
print("Error Counts:")
for error, count in error_count.items():
    print(error, ":", count)
