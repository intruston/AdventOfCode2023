import re

def process_strings_from_file(file_path):
    all_extracted_numbers = []
    modified_numbers = []
    total_sum = 0

#words dictionary
    mapping = {n: str(i % 9 + 1) for i, n in enumerate('1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine'.split('|'))}

    with open(file_path, 'r') as file:
        for line in file:
            #find all words and numbers (\d)
            matches = re.findall(r'(one|two|three|four|five|six|seven|eight|nine|\d)', line)
            # Add the condition for "twone" explicitly
            all_extracted_numbers.extend(matches)
            modified_number = '00'

            if matches:
                first_digit = next((match for match in matches if match.isdigit() or match.isalpha()), None)

                spelled_out_numbers = [word for word in matches if word.isalpha() or word.isdigit()]

                if spelled_out_numbers and first_digit:
                    last_spelled_out = spelled_out_numbers[-1]
                    modified_number = str(int(mapping[first_digit] + mapping[last_spelled_out])).zfill(2)
                elif first_digit:
                    modified_number = str(int(first_digit + first_digit)).zfill(2)

                total_sum += int(modified_number)  #accumulate the sum

            modified_numbers.append(modified_number)

    return all_extracted_numbers, modified_numbers, str(total_sum)

#deal with twone and oneight manually
file_path = 'input2.txt'
extracted_numbers, modified_numbers, total_sum = process_strings_from_file(file_path)

print("Extracted Numbers:", extracted_numbers)
print("Modified Numbers:", modified_numbers)
print("Length Numbers:", len(extracted_numbers))
print("Sum of All Modified Numbers:", total_sum)
