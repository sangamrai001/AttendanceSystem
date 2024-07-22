import os
import face_recognition
from PIL import Image


def face_extract(input_folder, current_date):

    # Create the output folder if it doesn't exist
    output_folder = current_date
    os.makedirs(output_folder, exist_ok=True)

    # List all image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    i = 0  # Initialize the counter for numbering the extracted faces

    for image_file in image_files:
        # Load the image from the input folder
        image_path = os.path.join(input_folder, image_file)
        group_image = face_recognition.load_image_file(image_path)
        face_locations = face_recognition.face_locations(group_image)

        print(f"Extracting faces from {image_file} ...............")

        for face_location in face_locations:
            top, right, bottom, left = face_location

            # Extract the face from the group photo
            face_image = group_image[top:bottom, left:right]

            # Convert the NumPy array to a Pillow image
            face_pillow_image = Image.fromarray(face_image)

            # Save the extracted face in the output folder with a sequential number
            output_path = os.path.join(output_folder, f"{current_date}_{i+1}.jpg")
            face_pillow_image.save(output_path)
            i += 1

        print(f"Face extraction from {image_file} done.....................")
    print("Face extraction from all images in the folder is complete.")
    return output_folder
