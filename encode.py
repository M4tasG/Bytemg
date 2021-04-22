from PIL import Image, ImageDraw

def convert_to_binary(byte_array):
    byte_list = []
    for byte in byte_array:
        byte = bin(byte)
        byte_list.append(byte)
    return byte_list

text = input()
text = convert_to_binary(bytearray(text, "utf8"))

img = Image.new('1', (8, len(text)))
draw = ImageDraw.Draw(img)


print(text)