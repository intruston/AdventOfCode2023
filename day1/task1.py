import re

def process_strings_from_file(file_path):
    all_extracted_numbers = []
    modified_numbers = []
    total_sum = 0

    with open(file_path, 'r') as file:
        for line in file:
            # Extract all digits from the string
            numbers = [int(digit) for digit in re.findall(r'\d', line)]
            all_extracted_numbers.extend(numbers)

            if len(numbers) >= 1:
                # Take the first and last digit
                modified_number = str(numbers[0]) + str(numbers[-1])
                # Modified number has exactly two digits
                modified_numbers.append(modified_number[:2])
            else:
                modified_numbers.append('00')

    # Total sum
    total_sum = sum(int(num) for num in modified_numbers)

    return all_extracted_numbers, modified_numbers, str(total_sum)

file_path = 'input1.txt'
extracted_numbers, modified_numbers, total_sum = process_strings_from_file(file_path)

print("Extracted Numbers:", extracted_numbers)
print("Modified Numbers:", modified_numbers)
print("Length Numbers:", len(extracted_numbers))
print("Sum of All Modified Numbers:", total_sum)
