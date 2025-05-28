from PIL import Image, ImageDraw

# Define the image size (CGSize(width: 3744 + 80, height: 5616 + 100 * 3))
width = 3744 + 80
height = 5616 + 100 * 3

# Number of horizontal grayscale bands
bands = 16
band_height = height // bands

# Create a new grayscale image ('L' mode)
image = Image.new("L", (width, height), color=0)
draw = ImageDraw.Draw(image)

# Draw each band from white to black
for i in range(bands):
    gray_value = int((1 - i / (bands - 1)) * 255)  # 255 = white, 0 = black
    y0 = i * band_height
    y1 = (i + 1) * band_height
    draw.rectangle([0, y0, width, y1], fill=gray_value)

# Show the image
image.show()

# Optionally save it
# image.save("grayscale_bands.png")