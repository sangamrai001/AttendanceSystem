import os
import face_recognition


def encode_images_in_folder(folder_path):
    # Create lists to store face encodings and corresponding image paths
    face_encodings = []
    print("Encoding test images..................")
    # Loop through files in the folder
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

            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")
    print("encodings generated..................")
    return face_encodings
