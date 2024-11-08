from PIL import Image, ImageDraw


def make_circular_image(input_path, output_path):
    # Load the image and convert it to RGBA mode (to ensure transparency support)
    img = Image.open(input_path).convert("RGBA")

    # Create a circular mask
    size = img.size
    mask = Image.new("L", size, 0)
    mask_draw = ImageDraw.Draw(mask)

    # Draw a white-filled circle in the center of the mask
    center_x, center_y = size[0] // 2, size[1] // 2
    radius = min(center_x, center_y)
    mask_draw.ellipse((center_x - radius, center_y - radius, center_x + radius, center_y + radius), fill=255)

    # Apply the circular mask to the image
    circular_img = Image.new("RGBA", size)
    circular_img.paste(img, (0, 0), mask=mask)

    # Save the result
    circular_img.save(output_path, "PNG")


# 사용 예시
make_circular_image("nav/4.png", "circular_4.png")
