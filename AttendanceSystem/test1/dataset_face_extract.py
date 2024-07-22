# THIS CODE IS TAKING AN GROUP PHOTO AND EXTRACT INDIVIDUAL FACES FROM IT AND STORE IT IN A FOLDER
import face_recognition
from PIL import Image
import os


def face_extract(input_folder):
    # Create the output folder if it doesn't exist
    output_folder = "dataset"
    os.makedirs(output_folder, exist_ok=True)

    # List all image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    i = 0  # Initialize the counter for numbering the extracted faces

    for image_file in image_files:
        # Load the image from the input folder
        image_path = os.path.join(input_folder, image_file)
        group_image = face_recognition.load_image_file(image_path)
        face_locations = face_recognition.face_locations(group_image)

        for face_location in face_locations:
            top, right, bottom, left = face_location

            # Extract the face from the group photo
            face_image = group_image[top:bottom, left:right]

            # Convert the NumPy array to a Pillow image
            face_pillow_image = Image.fromarray(face_image)

            roll_base = 202101
            roll_no = roll_base + i
            # Save the extracted face in the output folder with a sequential number
            output_path = os.path.join(output_folder, f"{roll_no}.jpg")
            face_pillow_image.save(output_path)
            i += 1


# Load the group photo
input_f = "data1"  # Change to the actual file path of your group photo
face_extract(input_f)

# this code is working all good and fine
