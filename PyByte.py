from PIL import Image

def compress_image(quality):
    # Open the JPEG image
    image = Image.open('input.jpg')

    # Save the compressed image as a new JPEG file
    image.save('compressed.jpg', quality=quality)

print("Welcome to PyByte")
# Ask for compression quality
quality = int(input("Enter the compression quality (1-100): "))
# Validate the input
if quality < 1 or quality > 100:
    print("Invalid compression quality. Please enter a value between 1 and 100.")
else:
    compress_image(quality)
    print("Image compressed successfully!")
