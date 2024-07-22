import csv
import os


def is_empty(file_path):
    return os.stat(file_path).st_size == 0


def roll(roll_numbers):
    # Check if the CSV file is empty
    if is_empty('attendance.csv'):
        # Open the existing CSV file in write mode
        with open('attendance.csv', mode='w', newline='') as file:
            writer = csv.writer(file)

            # Write "Roll Number" to A1
            writer.writerow(["Roll Number"])

            # Write the roll numbers to the first column
            for roll_number in roll_numbers:
                writer.writerow([roll_number])
