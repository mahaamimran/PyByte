from PIL import Image

# Open the JPEG image
image = Image.open('input.jpg')

# Set the desired compression quality (1-100)
compression_quality = 15

# Save the compressed image as a new JPEG file
image.save('compressed.jpg', quality=compression_quality)
