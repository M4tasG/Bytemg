from PIL import Image

def split_byte_to_nums(text):
    num_list = []
    for char in text:
        num_list.append(int(char))
    return num_list

def convert_to_binary(byte_array):
    byte_list = []
    for byte in byte_array:
        byte = bin(byte)
        byte_list.append(byte)
    return byte_list

def parse_byte_to_str(byte_list):
    parsed_list = []
    for byte in byte_list:
        byte = str(byte).replace('b','')
        parsed_list.append(byte)
    return parsed_list

def draw_bytes(byte_list):
    img = Image.new('1', (8, len(text)))
    #draw = ImageDraw.Draw(img)
    x = 0
    y = 0
    #i = 0
    for byte in byte_list:
        split_byte = split_byte_to_nums(byte)
        for byte in split_byte:
            print(byte)
            if(byte):
                img.putpixel((x,y), 0)
            else:
                img.putpixel((x,y), 255)
            x += 1
        x = 0
        y += 1
    img.save('encoded.jpg')

text = input()
text = convert_to_binary(bytearray(text, "utf8"))
text = parse_byte_to_str(text)
draw_bytes(text)



print(text)