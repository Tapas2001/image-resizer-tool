from PIL import Image

# Open an image
img = Image.open("resized_images/img1.jpg")

# Get image dimension(size)
dimension = img.size
print(dimension)

# format of the image
print(img.format)

# mode of the image
print(img.mode)

# Resized the image
resized_img = img.resize((200, 200))

# Save the resized image
resized_img.save('img.png')


# Save the resized image
# resized_img.show()


# Apply a filter (e.g., grayscale)
grayscale_img = img.convert("L")
grayscale_img.save("grayscale_example.jpg")



