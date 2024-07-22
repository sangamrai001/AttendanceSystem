# THIS CODE TAKES THE FOLDER HAVING IMAGES OF INDIVIDUAL FACES AND ENCODE THEM AND WRITE THEM INTO A TEXT FILE
import os
import face_recognition


def dataset_encoder(folder_path):
    # Create lists to store face encodings and corresponding image paths
    face_encodings = []
    image_path = []

    # Loop through files in the folder
    print("Encoding dataset faces.......")
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if the file is an image (you can add more image formats if needed)
        if file_path.lower().endswith(".jpg"):

            try:
                # Load the image using face_recognition
                image = face_recognition.load_image_file(file_path)

                # Find all face locations in the image
                face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=2)

                # Check if at least one face was found
                if len(face_locations) == 0:
                    print("No faces were found in the provided image.")
                else:
                    # Encode the first found face (you can modify this to encode multiple faces)
                    face_encoding = face_recognition.face_encodings(image, [face_locations[0]])[0]
                    face_encodings.append(face_encoding)
                    image_path.append(filename.replace(".jpg", ""))

            except Exception as e1:
                print(f"Error processing {filename}: {str(e1)}")
    return face_encodings, image_path


folder_path1 = "dataset"
encodings, roll_no = dataset_encoder(folder_path1)

# Specify the file path where you want to write the array data
file_path1 = "dataset_encodings.txt"

try:
    # Open the file for writing
    with open(file_path1, 'w') as file:
        # Write the array as a string with square brackets and commas
        for i in range(len(roll_no)):
            file.write(str(roll_no[i]) + '\n')
            file.write("[" + ", ".join(map(str, encodings[i])) + "]\n")
    print(f"NumPy array has been written to {file_path1}")
except IOError as e:
    print(f"Error writing to file: {e}")
