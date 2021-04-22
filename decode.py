from PIL import Image

def get_pixel_list(image):
    width = image.width
    height = image.height
    pixel_list = []
    pixel_temp = ""
    #x = 0
    #y = 0
    for pixel in range(height):
        for px in range(width):
            #print(f'x: {px} y: {pixel}')
            px = image.getpixel((px, pixel))
            #print(f'Color value: {px}')
            if(px > 125):
                px = 0
            else:
                px = 1
            pixel_temp += str(px)
            #x += 1
        pixel_list.append(pixel_temp)
        pixel_temp = ""
        #y += 1
    return pixel_list

def parse_bytes_to_char(byte_list):
    char_list = []
    for byte in byte_list:
        byte = int(byte, 2)
        byte_num = byte.bit_length() + 7 // 8
        bin_array = byte.to_bytes(byte_num, "big")
        char_list.append(bin_array.decode()[-1:])
    return char_list

def join_chars_to_str(char_list):
    _str = ""
    for char in char_list:
        _str += char
    return _str
img = Image.open('encoded.jpg')
pixels = get_pixel_list(img)
pixels = parse_bytes_to_char(pixels)
pixels = join_chars_to_str(pixels)
print(pixels)