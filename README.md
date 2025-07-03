# 🖼️ Image Resizer Tool

A simple Python script to batch resize and convert images in a folder using the Pillow library.

## 📌 Features
- Resize and convert all images in a specified folder to a fixed size.
- Supports multiple formats: `.png`, `.jpg`, `.jpeg`
- Skips non-image files.
- Basic error handling during processing.

## 🛠️ Requirements
- Python 3.x
- Pillow

Install dependencies using:
bash
`pip install Pillow `

## 📂 Folder Structure
bash
image-resizer-tool/
├── image_resizer.py
├── input_images/        # Put your original images here
├── resized_images/      # Output will be saved here
└── test.py              # For practice

## 🚀 Usage
Run the script from the terminal:
bash
python image_resizer.py

By default:

- It resizes images from the input_images/ folder.
- Outputs them to the resized_images/ folder.
- Uses size (800, 800) as default.

## 🔧 Customization
You can modify these variables in the script:
python
input_folder = "input_images"
output_folder = "resized_images"
target_size = (800, 800)
