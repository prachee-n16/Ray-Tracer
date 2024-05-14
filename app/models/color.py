from app.models.vec3 import vec3

color = vec3

def write_color(pixel_color):
    r = pixel_color.x
    g = pixel_color.y
    b = pixel_color.z

    rByte = int(255.999 * r)
    gByte = int(255.999 * g)
    bByte = int(255.999 * b)

    return f'{rByte} {gByte} {bByte} \n'