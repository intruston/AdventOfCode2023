import re

def process_strings_from_file(file_path):
    all_extracted_numbers = []
    modified_numbers = []
    total_sum = 0

    mapping = {n: str(i % 9 + 1) for i, n in enumerate('1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine'.split('|'))}

    with open(file_path, 'r') as file:
        for line in file:
            matches = re.findall(r'(one|two|three|four|five|six|seven|eight|nine|\d)', line)
            all_extracted_numbers.extend(matches)

            modified_number = '00'

            if matches:
                first_digit = next((match for match in matches if match.isdigit() or match.isalpha()), None)

                spelled_out_numbers = [word for word in matches if word.isalpha()]

                if spelled_out_numbers and first_digit:
                    last_spelled_out = spelled_out_numbers[-1]
                    modified_number = str(int(mapping[first_digit] + mapping[last_spelled_out])).zfill(2)
                elif first_digit:
                    modified_number = str(int(first_digit + first_digit)).zfill(2)

            modified_numbers.append(modified_number)

    total_sum = sum(int(num) for num in modified_numbers)

    return all_extracted_numbers, modified_numbers, str(total_sum)

file_path = 'input1.txt'
extracted_numbers, modified_numbers, total_sum = process_strings_from_file(file_path)

print("Extracted Numbers:", extracted_numbers)
print("Modified Numbers:", modified_numbers)
print("Length Numbers:", len(extracted_numbers))
print("Sum of All Modified Numbers:", total_sum)
