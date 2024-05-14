# This file tests the generation of an image with PPM Output format

def render_image(img_width: int, img_height: int) -> str:
    # Render image
    image_data = f"P3\n {img_width} {img_height}\n255\n"
    
    for j in range(0, img_height):
        for i in range(0, img_width):
            r = float(i) / (img_width - 1)
            g = float(j) / (img_height - 1)
            b = 0.0

            ir: int = int(255.999 * r)
            ig: int = int(255.999 * g)
            ib: int = int(255.999 * b)

            image_data += f"{ir} {ig} {ib}\n"

    return image_data