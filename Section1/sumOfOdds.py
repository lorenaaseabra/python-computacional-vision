import csv

def sum_of_odds(file_name):
    try:
        with open(file_name, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            odd_sum = 0

            for row in csv_reader:
                for num_str in row:
                    num = int(num_str)
                    if num % 2 != 0:
                        odd_sum += num

            return odd_sum
    except FileNotFoundError:
        print(f"The file '{file_name}' was not found.")
        return None
    except ValueError:
        print("The file contains values that are not integers.")
        return None


full_file_name = 'Section1/numeros.csv'
result = sum_of_odds(full_file_name)

if result is not None:
    file_name = full_file_name.split('/')[-1]
    print(f"The sum of odd numbers in the file '{file_name}' is: {result}")
