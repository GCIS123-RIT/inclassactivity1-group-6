import csv

def load_data():
    """
    Loads data from a CSV file, allowing the user to select a numerical column.

    Returns:
    list: Loaded column of numerical data as string datatype.
    """
    with open("sales.csv") as csv_file:
        csv_reader = csv.reader(csv_file)
        columns = next(csv_reader)  # Skips header
        for record in csv_reader:
            print(record)
    index = column_index_of(columns)
    while not column_is_numerical(index):
        index = column_index_of(columns)
    return load_column(index)

def column_index_of(columns):
    """
    Finds the index of a selected column from the CSV file.

    Args:
    columns (list): Array of column names.

    Returns:
    int: Index of the selected column.
    """
    print("Choose column:", columns)
    column_name = input("Please enter the exact name of the column: ")
    for i in columns:
        if column_name == i.strip():
            return columns.index(i)

def column_is_numerical(index):
    """
    Checks if a column is numerical.

    Args:
    index (int): Index of the column to check.

    Returns:
    bool: True if the column is numerical, False otherwise.
    """
    with open("sales.csv") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip header
        for record in csv_reader:
            try:
                float(record[index])
                print("Column is numerical")
                return True
            except ValueError:
                print("Column is not numerical or doesn't exist")
                return False

def load_column(index):
    """
    Loads the column from file to the array and returns array.

    Args:
    index (int): Index of the column to load.

    Returns:
    list: Loaded column.
    """
    loaded_column = []
    with open("sales.csv") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip header
        for record in csv_reader:
            loaded_column.append(record[index])
    print("Loaded values:", loaded_column)
    return loaded_column

def clean_replace_data(loaded_column):
    """
    Allows the user to choose to replace empty values with the minimum, maximum, or average of the column.

    Args:
    loaded_column (list): List of loaded column data.

    Returns:
    list: Complete column after replacing empty values.
    """
    complete_column = []
    print("Do you want to replace data with:\n1. Minimum\n2. Maximum\n3. Average")
    answer = input("Please enter option number: ")
    while answer not in ['1', '2', '3']:
        print("Incorrect input!")
        answer = input("Please enter the number of the option: ")
    if answer == '1':
        value = find_min(loaded_column)
    elif answer == '2':
        value = find_max(loaded_column)
    else:
        value = find_avg(loaded_column)
    complete_column = exchange_with_value(loaded_column, value)
    print(complete_column)
    return complete_column

def find_min(loaded_column):
    """
    Finds the minimum value in a column.

    Args:
    loaded_column (list): List of loaded column data.

    Returns:
    float: Minimum value.
    """
    minimum = float('inf')
    for i in loaded_column:
        if i.strip():
            minimum = min(minimum, float(i.strip()))
    return minimum

def find_max(loaded_column):
    """
    Finds the maximum value in a column.

    Args:
    loaded_column (list): List of loaded column data.

    Returns:
    float: Maximum value.
    """
    maximum = float('-inf')
    for i in loaded_column:
        if i.strip():
            maximum = max(maximum, float(i.strip()))
    return maximum

def find_avg(loaded_column):
    """
    Finds the average value in a column.

    Args:
    loaded_column (list): List of loaded column data.

    Returns:
    float: Average value.
    """
    total = 0
    count = 0
    for i in loaded_column:
        if i.strip():
            total += float(i.strip())
            count += 1
    if count != 0:
        return total / count
    return 0  # To avoid division by zero if all values are empty

def exchange_with_value(loaded_column, value):
    """
    Replaces empty values in a column with a specified value.

    Args:
    loaded_column (list): List of loaded column data.
    value (float): Value to replace empty values with.

    Returns:
    list: Column after replacing empty values.
    """
    numerical_column = []
    for i in loaded_column:
        if not i.strip():
            numerical_column.append(value)
        else:
            numerical_column.append(float(i.strip()))
    return numerical_column

def analyse_data(numerical_column):
    """
    Sorts the data in ascending or descending order based on user input.

    Args:
    numerical_column (list): List of numerical data.

    Returns:
    list: Sorted data.
    """
    print("Please choose if you would like to sort the data in:\n1. Ascending\n2. Descending")
    answer = input("Please enter the number of the option: ")
    while answer not in ['1', '2']:
        print("Incorrect input!")
        answer = input("Please enter the number of the option: ")
    if answer == '1':
        numerical_column = sorted(numerical_column)
    else:
        numerical_column = sorted(numerical_column, reverse=True)
    print('Data after analyzing:', numerical_column)
    return numerical_column

def visualize_data(numerical_column):
    """
    Visualizes the data by printing asterisks corresponding to the values.

    Args:
    numerical_column (list): List of numerical data.
    """
    print("Visualizing data")
    for i in numerical_column:
        if i > 100:
            i = 100  # Limiter to 100 for visualization purposes
        print('*' * int(i))

def main():
    """
    Main function running all the phases.
    """
    print("\n################ Phase 1 - Loading ################")
    loaded_column = load_data()
    print("\n################ Phase 2 - Cleaning ################")
    clean_data = clean_replace_data(loaded_column)
    print("\n################ Phase 3 - Analyzing ################")
    sorted_data = analyse_data(clean_data)
    print("\n################ Phase 4 - Visualizing ################")
    visualize_data(sorted_data)

main()
