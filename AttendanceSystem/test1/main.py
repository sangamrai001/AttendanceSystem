from encoder import *
from face_extract import *
from matcher import *
from attend import *
from rollno import *
from datetime import datetime

# Initialize empty arrays for odd and even lines
odd_lines = []
even_lines = []

# Open the file in read mode
file_path = 'dataset_encodings.txt'  # Replace with the path to your file
try:
    with open(file_path, 'r') as file:
        # Initialize a line counter
        line_number = 1

        # Iterate through each line in the file
        for line in file:
            # Determine if the current line is odd or even
            if line_number % 2 == 1:
                odd_lines.append(line.strip())
            else:
                even_lines.append(line.strip())

            # Increment the line counter
            line_number += 1
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

roll_no = [int(element) for element in odd_lines]
roll(roll_no)
roll_no2 = roll_no.copy()
encoding = []
for i in range(len(even_lines)):
    elements = even_lines[i].strip('[]').split(',')
    float_array = np.array([float(element.strip()) for element in elements])
    encoding.append(float_array)

date = datetime.now().strftime("%d-%m-%Y")
today_date = f"{date}"
test_folder = f"test_{date}"

folder_name = face_extract(test_folder, today_date)
encodings = encode_images_in_folder(folder_name)
matched_indexes = find_best_matches(encodings, encoding, tolerance=0.6)
attend(roll_no, matched_indexes, date)
