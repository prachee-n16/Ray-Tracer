from app.examples.ppm_v2 import render_image
from app.utils import save_file_contents
from app.models.vec3 import vec3, unit_vector
DEBUG = False

def main():
    # Image dimensions 
    img_width: int = 256
    img_height: int = 256

    img_data = render_image(img_width, img_height)
    save_file_contents("./images/output.ppm", img_data)

if __name__ == "__main__":
    main()