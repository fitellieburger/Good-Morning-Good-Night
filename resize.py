from PIL import Image
import os

input_folder = "stickers"
output_folder = "newStickers"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    input_path = os.path.join(input_folder, filename)
    if os.path.isfile(input_path):
        # Open the input image using Pillow
        with Image.open(input_path) as im:
            # Resize the image to 60x60 pixels using antialiasing to preserve image quality
            resized_im = im.resize((60, 60), resample=Image.LANCZOS)

            # Save the resized image to the output folder
            output_path = os.path.join(output_folder, filename)
            resized_im.save(output_path)
