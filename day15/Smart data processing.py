import numpy as np
import pandas as pd
import time

# ✅ Decorator to measure execution time
def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution Time: {end - start:.5f} seconds")
        return result
    return wrapper


# ✅ Generator to read numbers from file
def read_numbers(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                try:
                    yield float(line.strip())   # convert to number
                except ValueError:
                    print(f"Skipping invalid data: {line.strip()}")
    except FileNotFoundError:
        print("File not found!")


# ✅ Main processing function
@measure_time
def process_data(file_name):
    data = []

    # Stream data using generator
    for num in read_numbers(file_name):
        data.append(num)

    if len(data) == 0:
        print("No valid data found!")
        return

    # Convert to NumPy array
    arr = np.array(data)

    # NumPy calculations
    mean_val = np.mean(arr)
    std_val = np.std(arr)

    # Convert to Pandas DataFrame
    df = pd.DataFrame({
        "Metric": ["Mean", "Standard Deviation"],
        "Value": [mean_val, std_val]
    })

    return df


# ✅ Run the pipeline
result = process_data("data.txt")

if result is not None:
    print("\nFinal DataFrame:")
    print(result)
