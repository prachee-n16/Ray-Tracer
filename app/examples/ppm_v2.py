# This file tests the generation of an image with PPM Output format
from app.models.color import color, write_color

def render_image(img_width: int, img_height: int) -> str:
    # Render image
    image_data = f"P3\n {img_width} {img_height}\n255\n"
    
    for j in range(0, img_height):
        for i in range(0, img_width):
            pixel_color = color(float(i)/(img_width - 1), float(j)/(img_height - 1), 0)
            image_data += write_color(pixel_color)

    return image_data