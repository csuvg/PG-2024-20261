import csv

# ----------------- Store CSV ----------------- #
# Function: store_csv
# Description: Writes data to a csv file
# Parameters:
#       - file: name of the file to write to
#       - data: data to write to file
# Return: None
# ----------------------------------------------- #
def store_csv(file, data):

    try:                                                                                # Check if file exists
        with open(file, mode='r', newline='\n', encoding='utf-8') as f:                 # Try to open file in read-only mode
            pass

    except FileNotFoundError:                                                           # If file does not exist       
        with open(file, mode='w', newline='\n', encoding='utf-8') as f:                 # Create file
            writer = csv.writer(f)                                                      # Create writer object
            writer.writerow(['LENSEGUA', 'ESPAÑOL'])                                    # Write headers to file

    with open(file, mode='a', newline='\n', encoding='utf-8') as f:                     # Open file in append mode
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)                                   # Create writer object

        for row in data:                                                                # Iterate through data 
            writer.writerow(row)                                                        # Write data to file

# ----------------- Input Data ----------------- #
# Function: input_data
# Description: Allows user to input data through the console
# Parameters: None
# Return:
#       - data: data input by user
# ----------------------------------------------- #
def input_data():
    
    data = []                                                                           # Initialize data list

    while True:                                                                         # Loop until user decides to stop
        lensegua = input("LENSEGUA: ")                                                  # Ask user for lensegua sentence
        spanish = input('\nESPAÑOL: ')                                                  # Ask user for spanish translation

        lensegua = lensegua.strip()                                                     # Remove leading/trailing whitespaces
        spanish = spanish.strip()

        if lensegua == 'exit' or spanish == 'exit':                                     # If user types 'exit'
            break                                                                       # Break loop

        data.append([lensegua, spanish])                                                # Add data to list

        print("\n ----------------- \n")

    return data                                                                         # Return data


# ----------------- Main ----------------- #
# Description: Reads data from user and stores it in a csv file
# Parameters: None
# Return: None
# -------------------------------------- #
def main():
    file = './SenasChapinas_ProcesamientoDeLenguajeNatural/src/dataset/raw/dataset.csv' # Name of file to write to
    data = input_data()                                                                 # Get data from user
    store_csv(file, data)                                                               # Store data in file


if __name__ == '__main__':
    main()