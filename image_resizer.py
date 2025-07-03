import os
from PIL import Image

# Congiguration
input_folder = "input_images"    # Folder containing original images
output_folder = "resized_images"  # Folder to save images
target_size = (800, 800)          # Resize target (width, height)


def resize_images():
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            print(f"Skipping non-image file: {filename}")
            continue

        try:
            with Image.open(input_path) as img:
                img_resized = img.resize(target_size)
                base_name = filename.split('.')[0]
                print(base_name)
                print(img.format)
                if img.format in ('JPEG', 'JPG'): 
                    output_path = os.path.join(output_folder, f'{base_name}.png')
                else:
                    output_path = os.path.join(output_folder, f'{base_name}.jpg')
                print(output_path)
                img_resized.save(output_path)
                print(f"Resized and save: {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")


if __name__ == "__main__":
    resize_images()

