import csv


def attend(roll_no, matched_indexes, date):
    csv_file = 'attendance.csv'  # Assuming you're using a fixed file name

    # Open the existing CSV file in read mode
    with open(csv_file, 'r', newline='') as file:
        # Read the existing data
        reader = csv.reader(file)
        data = list(reader)

    # Find the index of the current date or add it if not present
    if date not in data[0]:
        data[0].append(date)
        date_index = len(data[0]) - 1
        for row in data[1:]:
            row.append('Absent')  # Add 'Absent' for existing rows
    else:
        date_index = data[0].index(date)

    # Iterate through the roll numbers
    for index in matched_indexes:
        roll_number = roll_no[index]
        for row in data[1:]:
            if row[0] == str(roll_number):
                # Mark attendance for this roll number
                row[date_index] = 'Present'
                break

    # Open the CSV file in write mode
    with open(csv_file, 'w', newline='') as file:
        # Write the modified data back to the file
        writer = csv.writer(file)
        writer.writerows(data)

    print(f"Attendance marked successfully for {date}.................")
